import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px
from django_plotly_dash import DjangoDash
from .models import Certifications

# Créer l'app Dash
app = DjangoDash('CertificationsDashboard')

# Charger les données
def get_certifications_data():
    certifications = Certifications.objects.all()
    data = []

    for cert in certifications:
        data.append({
            "name": cert.name,
            "level": dict(Certifications._meta.get_field('level_of_difficulty').choices).get(cert.level_of_difficulty),
            "price": float(cert.price),
            "institution": cert.institution.name if cert.institution else None,
        })
    return pd.DataFrame(data)

df = get_certifications_data()

# Graphique 1 : Nombre de certifications par niveau
fig_level = px.histogram(df, x='level', title="Certifications par niveau de difficulté")

# Graphique 2 : Prix moyen par niveau
fig_price = px.box(df, x='level', y='price', title="Prix par niveau de difficulté")

# Layout de l'app Dash
app.layout = html.Div([
    html.H1("📊 Tableau de bord des Certifications", style={"textAlign": "center"}),

    dcc.Graph(figure=fig_level),
    dcc.Graph(figure=fig_price),
])
