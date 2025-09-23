"""
Custom analytics tools for the ETUGRAND AgentOS analytics agent.
Provides advanced data analysis, visualization, and reporting capabilities.
"""

import json
import os
from typing import Dict, List, Any, Optional, Union
from datetime import datetime, timedelta
import re

try:
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    import plotly.graph_objects as go
    import plotly.express as px
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.linear_model import LinearRegression
    from sklearn.preprocessing import StandardScaler
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_squared_error, r2_score
    ANALYTICS_AVAILABLE = True
except ImportError:
    ANALYTICS_AVAILABLE = False


class AnalyticsTools:
    """Advanced analytics tools for data analysis and visualization."""

    def __init__(self):
        self.data_cache = {}
        self.report_cache = {}

    def analyze_performance_metrics(self, metrics_data: str) -> str:
        """
        Analyze performance metrics and provide insights.

        Args:
            metrics_data: JSON string containing performance metrics

        Returns:
            JSON string with analysis results and insights
        """
        if not ANALYTICS_AVAILABLE:
            return json.dumps({"error": "Analytics libraries not available"})

        try:
            data = json.loads(metrics_data)

            # Convert to DataFrame for analysis
            df = pd.DataFrame(data)

            # Calculate basic statistics
            analysis = {
                "summary": {
                    "total_records": len(df),
                    "date_range": {
                        "start": df.get('date', pd.Series([datetime.now().isoformat()])).min(),
                        "end": df.get('date', pd.Series([datetime.now().isoformat()])).max()
                    }
                },
                "metrics": {},
                "insights": [],
                "trends": {}
            }

            # Analyze numeric columns
            numeric_cols = df.select_dtypes(include=[np.number]).columns

            for col in numeric_cols:
                if col in df.columns:
                    analysis["metrics"][col] = {
                        "mean": float(df[col].mean()),
                        "median": float(df[col].median()),
                        "std": float(df[col].std()),
                        "min": float(df[col].min()),
                        "max": float(df[col].max()),
                        "trend": self._calculate_trend(df[col])
                    }

                    # Generate insights
                    if df[col].std() / df[col].mean() > 0.5:
                        analysis["insights"].append(f"High variability in {col} (CV: {df[col].std()/df[col].mean():.2f})")

                    if self._calculate_trend(df[col]) > 0.1:
                        analysis["insights"].append(f"Positive trend detected in {col}")
                    elif self._calculate_trend(df[col]) < -0.1:
                        analysis["insights"].append(f"Negative trend detected in {col}")

            # Calculate correlations
            if len(numeric_cols) > 1:
                corr_matrix = df[numeric_cols].corr()
                strong_correlations = []

                for i, col1 in enumerate(numeric_cols):
                    for j, col2 in enumerate(numeric_cols):
                        if i < j and abs(corr_matrix.iloc[i, j]) > 0.7:
                            strong_correlations.append({
                                "metric1": col1,
                                "metric2": col2,
                                "correlation": float(corr_matrix.iloc[i, j])
                            })

                analysis["correlations"] = strong_correlations

                if strong_correlations:
                    analysis["insights"].append(f"Found {len(strong_correlations)} strong correlations between metrics")

            return json.dumps(analysis, indent=2)

        except Exception as e:
            return json.dumps({"error": f"Analysis failed: {str(e)}"})

    def generate_forecast(self, historical_data: str, periods: int = 30) -> str:
        """
        Generate forecasts using machine learning models.

        Args:
            historical_data: JSON string with historical time series data
            periods: Number of periods to forecast

        Returns:
            JSON string with forecast results
        """
        if not ANALYTICS_AVAILABLE:
            return json.dumps({"error": "Analytics libraries not available"})

        try:
            data = json.loads(historical_data)
            df = pd.DataFrame(data)

            # Ensure we have date and value columns
            if 'date' not in df.columns or 'value' not in df.columns:
                return json.dumps({"error": "Data must contain 'date' and 'value' columns"})

            # Prepare data for modeling
            df['date'] = pd.to_datetime(df['date'])
            df = df.sort_values('date')

            # Create time-based features
            df['day_of_week'] = df['date'].dt.dayofweek
            df['day_of_month'] = df['date'].dt.day
            df['month'] = df['date'].dt.month
            df['quarter'] = df['date'].dt.quarter
            df['year'] = df['date'].dt.year

            # Create lag features
            df['lag_1'] = df['value'].shift(1)
            df['lag_7'] = df['value'].shift(7)

            # Drop rows with NaN values
            df = df.dropna()

            if len(df) < 10:
                return json.dumps({"error": "Insufficient data for forecasting"})

            # Prepare features and target
            feature_cols = ['day_of_week', 'day_of_month', 'month', 'quarter', 'year', 'lag_1', 'lag_7']
            X = df[feature_cols]
            y = df['value']

            # Split data
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Train models
            models = {
                'linear_regression': LinearRegression(),
                'random_forest': RandomForestRegressor(n_estimators=100, random_state=42)
            }

            results = {}

            for model_name, model in models.items():
                model.fit(X_train, y_train)
                y_pred = model.predict(X_test)

                mse = mean_squared_error(y_test, y_pred)
                r2 = r2_score(y_test, y_pred)

                results[model_name] = {
                    'mse': float(mse),
                    'r2': float(r2),
                    'accuracy': float(r2 * 100)
                }

                # Generate forecasts
                last_date = df['date'].max()
                forecast_dates = [last_date + timedelta(days=i) for i in range(1, periods + 1)]

                forecasts = []
                for forecast_date in forecast_dates:
                    features = {
                        'day_of_week': forecast_date.dayofweek,
                        'day_of_month': forecast_date.day,
                        'month': forecast_date.month,
                        'quarter': forecast_date.quarter,
                        'year': forecast_date.year,
                        'lag_1': df['value'].iloc[-1] if len(df) > 0 else 0,
                        'lag_7': df['value'].iloc[-7] if len(df) > 6 else 0
                    }

                    forecast_value = model.predict([list(features.values())])[0]
                    forecasts.append({
                        'date': forecast_date.isoformat(),
                        'forecast': float(forecast_value)
                    })

                results[model_name]['forecasts'] = forecasts

            # Select best model
            best_model = max(results.keys(), key=lambda x: results[x]['r2'])

            return json.dumps({
                'forecast_results': results,
                'best_model': best_model,
                'model_performance': results[best_model]['accuracy'],
                'summary': f"Generated {periods}-period forecast using {best_model} with {results[best_model]['accuracy']:.1f}% accuracy"
            })

        except Exception as e:
            return json.dumps({"error": f"Forecasting failed: {str(e)}"})

    def create_dashboard_data(self, data_sources: str) -> str:
        """
        Create dashboard-ready data with various chart types.

        Args:
            data_sources: JSON string containing data source information

        Returns:
            JSON string with dashboard data and visualizations
        """
        if not ANALYTICS_AVAILABLE:
            return json.dumps({"error": "Analytics libraries not available"})

        try:
            sources = json.loads(data_sources)
            dashboard_data = {
                "charts": {},
                "summary": {},
                "real_time_metrics": {}
            }

            for source_name, source_data in sources.items():
                df = pd.DataFrame(source_data)

                # Time series chart
                if 'date' in df.columns and any(col in df.columns for col in ['value', 'amount', 'count']):
                    value_col = next((col for col in ['value', 'amount', 'count'] if col in df.columns), None)
                    if value_col:
                        dashboard_data["charts"][f"{source_name}_timeseries"] = {
                            "type": "line",
                            "data": {
                                "x": df['date'].tolist(),
                                "y": df[value_col].tolist()
                            },
                            "title": f"{source_name} Over Time"
                        }

                # Distribution chart
                numeric_cols = df.select_dtypes(include=[np.number]).columns
                if len(numeric_cols) > 0:
                    for col in numeric_cols[:3]:  # Limit to first 3 numeric columns
                        dashboard_data["charts"][f"{source_name}_{col}_distribution"] = {
                            "type": "histogram",
                            "data": {
                                "values": df[col].tolist()
                            },
                            "title": f"Distribution of {col} in {source_name}"
                        }

                # Summary statistics
                dashboard_data["summary"][source_name] = {
                    "record_count": len(df),
                    "numeric_columns": len(numeric_cols),
                    "date_range": {
                        "start": df.get('date', pd.Series([datetime.now().isoformat()])).min(),
                        "end": df.get('date', pd.Series([datetime.now().isoformat()])).max()
                    } if 'date' in df.columns else None,
                    "metrics": {}
                }

                # Calculate metrics for numeric columns
                for col in numeric_cols:
                    dashboard_data["summary"][source_name]["metrics"][col] = {
                        "mean": float(df[col].mean()),
                        "median": float(df[col].median()),
                        "std": float(df[col].std()),
                        "min": float(df[col].min()),
                        "max": float(df[col].max())
                    }

                # Real-time metrics (latest values)
                if 'date' in df.columns:
                    latest_data = df.loc[df['date'].idxmax()]
                    dashboard_data["real_time_metrics"][source_name] = {
                        "latest_timestamp": latest_data.get('date', ''),
                        "latest_values": {col: float(latest_data[col]) for col in numeric_cols}
                    }

            return json.dumps(dashboard_data, indent=2)

        except Exception as e:
            return json.dumps({"error": f"Dashboard creation failed: {str(e)}"})

    def analyze_ab_test_results(self, test_data: str) -> str:
        """
        Analyze A/B test results for statistical significance.

        Args:
            test_data: JSON string containing A/B test data

        Returns:
            JSON string with A/B test analysis results
        """
        if not ANALYTICS_AVAILABLE:
            return json.dumps({"error": "Analytics libraries not available"})

        try:
            data = json.loads(test_data)
            df = pd.DataFrame(data)

            # Ensure required columns exist
            required_cols = ['group', 'metric', 'value']
            if not all(col in df.columns for col in required_cols):
                return json.dumps({"error": "Data must contain 'group', 'metric', and 'value' columns"})

            analysis_results = {}

            # Group by metric and analyze each
            for metric in df['metric'].unique():
                metric_data = df[df['metric'] == metric]

                # Separate groups
                group_a = metric_data[metric_data['group'] == 'A']['value']
                group_b = metric_data[metric_data['group'] == 'B']['value']

                if len(group_a) == 0 or len(group_b) == 0:
                    continue

                # Calculate statistics
                mean_a = group_a.mean()
                mean_b = group_b.mean()
                std_a = group_a.std()
                std_b = group_b.std()

                # Calculate effect size
                effect_size = (mean_b - mean_a) / ((std_a + std_b) / 2) if (std_a + std_b) > 0 else 0

                # Calculate t-test approximation
                pooled_std = ((len(group_a) - 1) * std_a**2 + (len(group_b) - 1) * std_b**2) / (len(group_a) + len(group_b) - 2)
                t_stat = (mean_b - mean_a) / (pooled_std**0.5 * (1/len(group_a) + 1/len(group_b))**0.5) if pooled_std > 0 else 0

                # Determine significance (simplified)
                significant = abs(t_stat) > 2.0  # Rough approximation for p < 0.05

                analysis_results[metric] = {
                    "group_a": {
                        "mean": float(mean_a),
                        "std": float(std_a),
                        "count": len(group_a)
                    },
                    "group_b": {
                        "mean": float(mean_b),
                        "std": float(std_b),
                        "count": len(group_b)
                    },
                    "improvement": float((mean_b - mean_a) / mean_a * 100) if mean_a != 0 else 0,
                    "effect_size": float(effect_size),
                    "t_statistic": float(t_stat),
                    "significant": significant,
                    "recommendation": "Implement Group B" if significant and mean_b > mean_a else "Continue current version"
                }

            return json.dumps({
                "ab_test_results": analysis_results,
                "summary": f"Analyzed {len(analysis_results)} metrics",
                "significant_findings": sum(1 for r in analysis_results.values() if r["significant"])
            })

        except Exception as e:
            return json.dumps({"error": f"A/B test analysis failed: {str(e)}"})

    def _calculate_trend(self, series: pd.Series) -> float:
        """Calculate trend coefficient for a time series."""
        if len(series) < 2:
            return 0.0

        x = np.arange(len(series))
        y = series.values

        # Remove NaN values
        mask = ~np.isnan(y)
        x = x[mask]
        y = y[mask]

        if len(x) < 2:
            return 0.0

        # Calculate linear trend
        trend = np.polyfit(x, y, 1)[0]
        return float(trend)