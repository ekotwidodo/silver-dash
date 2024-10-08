import plotly.graph_objects as go

# Function to plot population pyramid
def plot_pyramid(df, year):
  fig = go.Figure()

  # Add Male bars (make them negative for the left side of the chart)
  fig.add_trace(go.Bar(
      y=df["Age Group"],
      x=-df["Male"],  # Convert male values to negative for the left side
      name='Male',
      orientation='h',
      marker=dict(color='#1f77b4'),
      hovertemplate='Year: {year}<br>Population: %{customdata:,}<br>Age Group: %{y}<extra></extra>',
      customdata=df["Male"],  # Hover still shows positive values
  ))

  # Add Female bars (positive for the right side)
  fig.add_trace(go.Bar(
      y=df["Age Group"],
      x=df["Female"],
      name='Female',
      orientation='h',
      marker=dict(color='#ff7f0e'),
      hovertemplate='Year: {year}<br>Population: %{customdata:,}<br>Age Group: %{y}<extra></extra>',
      customdata=df["Female"],  # Hover shows positive values
  ))

  # Highlight the elderly age groups (60-64, 65-69, 70-74, 75-79, 80+)
  elderly_color_male = '#d62728'  # Red color for elderly population
  elderly_color_female = '#ff9896'  # Red color for elderly population
  elderly_groups = ["60-64", "65-69", "70-74", "75-79", "80+"]
  
  for age_group in elderly_groups:
      male_value = df.loc[df["Age Group"] == age_group, "Male"].values[0]
      female_value = df.loc[df["Age Group"] == age_group, "Female"].values[0]

      fig.add_trace(go.Bar(
          y=[age_group],
          x=[-male_value],  # Negative male value for left side
          name='Male (Elderly)',
          orientation='h',
          marker=dict(color=elderly_color_male),
          showlegend=False
      ))

      fig.add_trace(go.Bar(
          y=[age_group],
          x=[female_value],  # Positive female value for right side
          name='Female (Elderly)',
          orientation='h',
          marker=dict(color=elderly_color_female),
          showlegend=False
      ))

  # Add legend entry for the elderly population
  fig.add_trace(go.Bar(
      y=[None],  # Dummy entry to add the elderly color to the legend
      x=[None],
      name='Elderly Male (60+)',
      marker=dict(color=elderly_color_male),
      showlegend=True
  ))

  fig.add_trace(go.Bar(
      y=[None],  # Dummy entry to add the elderly color to the legend
      x=[None],
      name='Elderly Female (60+)',
      marker=dict(color=elderly_color_female),
      showlegend=True
  ))

  # Update layout for pyramid
  fig.update_layout(
      title=f"Population Pyramid for {year}",
      barmode='overlay',
      xaxis=dict(tickvals=[-35000, -25000, -15000, -5000, 0, 5000, 15000, 25000, 35000],
                  ticktext=['35K', '25K', '15K', '5K', '0', '5K', '15K', '25K', '35K']),
      xaxis_title='Population',
      yaxis_title='Age Group',
      template="plotly_white",
      plot_bgcolor='#f9f9f9',
      margin=dict(l=50, r=50, t=70, b=50),
      height=500,
      legend=dict(x=0.5, y=-0.2, xanchor='center', orientation="h")  # Legend at the bottom
  )

  return fig