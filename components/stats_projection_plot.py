import plotly.graph_objects as go

# Function to create a stylized line chart
def plot_population_projection(df):
  fig = go.Figure()

  # Adding line plot
  fig.add_trace(go.Scatter(
    x=df["Year"],
    y=df["Elderly Population"],
    mode="lines+markers",
    line=dict(shape='spline', smoothing=1.3, width=4, color='#ff7f0e'),  # Smooth and thick line with custom color
    marker=dict(size=8, color='#17BECF', line=dict(width=2, color='darkblue')),  # Stylish markers
    name="Population Projection",
    hovertemplate='<b>Year: %{x}</b><br>Elderly Population: %{y:,}%<extra></extra>'  # Custom hover info
  ))

  # Customizing the layout for a beautiful appearance
  fig.update_layout(
    title="Percentage of Elderly Population Projection 2020-2050",
    title_font=dict(size=22, color='darkblue', family="Arial"),
    xaxis_title="Year",
    yaxis_title="Elderly Population (%)",
    xaxis=dict(tickmode='linear', dtick=10),  # Setting ticks every 10 years
    yaxis=dict(tickformat=",", titlefont=dict(size=18, family="Arial")),
    template="plotly_white",
    plot_bgcolor='#f9f9f9',  # Light gray background for the plot area
    hovermode="x unified",  # Single hover showing all data at a specific x-value
    font=dict(family="Arial", size=14),
    margin=dict(l=50, r=50, b=50, t=70),
    legend=dict(x=0.8, y=1.1, orientation="h", bgcolor="rgba(0,0,0,0)")
  )
  return fig
