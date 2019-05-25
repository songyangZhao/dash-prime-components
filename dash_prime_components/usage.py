import dash_prime_components
import dash
from dash.dependencies import Input, Output
import dash_html_components as html

external_stylesheets = [
    'https://cdn.jsdelivr.net/npm/primereact@3.1.3/resources/themes/nova-light/theme.css',
    'https://cdn.jsdelivr.net/npm/primereact@3.1.3/resources/primereact.min.css',
    'https://cdn.jsdelivr.net/npm/primeicons@1.0.0/primeicons.css',
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.scripts.config.serve_locally = True
app.css.config.serve_locally = True


app.layout = html.Div([
    dash_prime_components.DashPrimeComponents(
        id='input',
        value='my-value',
        label='my-label'
    ),
    html.Div(id='output')
])

@app.callback(Output('output', 'children'), [Input('input', 'value')])
def display_output(value):
    return 'You have entered {}'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)
