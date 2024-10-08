import plotly.graph_objects as go

# Create a stacked bar chart function
def plot_stacked_bar_chart(df):
  # Sort the data by 'Working Elderly Living Alone'
  df = df.sort_values(by='Elderly (Working and Non Working) Living with Working Household', ascending=True)

  fig = go.Figure()
  # Add traces for each category
  fig.add_trace(go.Bar(
      y=df["Province"],
      x=df["Elderly (Working and Non Working) Living with Working Household"],
      name='Elderly (Working and Non Working) Living with Working Household',
      orientation='h',
      marker=dict(color='#d62728')  # Custom color
  ))

  fig.add_trace(go.Bar(
      y=df["Province"],
      x=df["Non Working Elderly Living with Non Working Household"],
      name='Non Working Elderly Living with Non Working Household',
      orientation='h',
      marker=dict(color='#ff7f0e')  # Custom color
  ))

  fig.add_trace(go.Bar(
      y=df["Province"],
      x=df["Working Elderly Living Alone"],
      name='Working Elderly Living Alone',
      orientation='h',
      marker=dict(color='#2ca02c')  # Custom color for each category
  ))

  fig.add_trace(go.Bar(
      y=df["Province"],
      x=df["Non Working Elderly Living Alone"],
      name='Non Working Elderly Living Alone',
      orientation='h',
      marker=dict(color='#1f77b4')  # Custom color
  ))  

  # Update layout for the stacked bar chart
  fig.update_layout(
      title="Elderly Population by Category and Province",
      barmode='stack',
      xaxis_title="Population",
      yaxis_title="Province",
      template="plotly_white",
      plot_bgcolor='#f9f9f9',
      legend=dict(
          x=0.5, y=-0.1,  # Position legend at the bottom
          xanchor='center',  # Center legend horizontally
          orientation="h"  # Horizontal legend
      ),
      margin=dict(l=100, r=50, t=70, b=100),  # Increase left margin for province labels
      width=1000,  # Set the chart width to be wider
      height=1000  # Adjust the height for better display
  )

  return fig
