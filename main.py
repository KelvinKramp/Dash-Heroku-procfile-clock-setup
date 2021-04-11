import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import json
import os
from clock import job
import threading as Threading

# START BACKGROUND JOB
print("Running timed job on the background through a thread")
t1 = Threading.Thread(target=job)
t1.start()
print("Timed job started")

# DEFINE VARIABLES
# starting input value
init_var = 90
time_interval_file_path = os.path.join("time_interval.json")

# APP
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div([
    html.H6("Change the value in the text box to see callbacks in action!"),
    html.Div(["Input: ",
              dcc.Input(id='my-input', value=init_var, type='text')]),
    html.Br(),
    html.Div(id='my-output'),

])

# CALLBACK
@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
def update_output_div(input_value):
    dict_input_time_intervals = {}
    dict_input_time_intervals["TIME-INTERVAL"] = str(input_value)
    with open(time_interval_file_path, 'w') as f:
        json.dump(dict_input_time_intervals, f)
    return 'Output: {}'.format(input_value)


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8080 ,debug=True)