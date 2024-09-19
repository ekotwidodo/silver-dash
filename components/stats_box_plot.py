import plotly.express as px
import plotly.graph_objects as go
def box_plot(df):
  # Convert percentage column from decimal to percentage
  df['pct_kesehatan'] = df['pct_kesehatan'] * 100

  fig = go.Figure()

  for household in df['ruta_lansia'].unique():
      fig.add_trace(go.Box(
          y=df[df['ruta_lansia'] == household]['pct_kesehatan'],
          name=household,
          boxmean=True,  # Add mean line
          fillcolor='lightblue' if household == 'Household with Elderly' else 'lightgreen'
      ))

  # Customize layout
  fig.update_layout(
      title='Proportion of Health Expenditure over Non-Food Household Expenditure, 2023',
      yaxis_title='Proportion (%)',
      xaxis_title='Household',
      yaxis=dict(
          tickmode='array',
          tickvals=list(range(0, 101, 10)),  # Set breaks from 0 to 100 with interval of 10
          range=[0, 100]  # Set limits from 0 to 100
      ),
      template='simple_white',  # Minimal theme
      showlegend=False  # Hide legend
  )
  return fig