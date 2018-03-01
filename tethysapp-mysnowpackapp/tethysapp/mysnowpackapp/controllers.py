from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime
import plotly.graph_objs as go
from tethys_sdk.gizmos import Button, PlotlyView, SelectInput, TimeSeries, TextInput

@login_required()
def home(request):
    """
    Controller for the app home page.
    """
    context = {

    }

    return render(request, 'mysnowpackapp/home.html', context)

def mapview(request):

    select_input = SelectInput(display_text='Select',
                               name='select1',
                               multiple=False,
                               original=True,
                               options=[('Davis County', '1'), ('Salt Lake County', '2'), ('Utah County', '3')],
                               initial=['Utah County'])

    x = [datetime(year=2017, month=01, day=01),
         datetime(year=2017, month=02, day=01),
         datetime(year=2017, month=03, day=01),
         datetime(year=2017, month=04, day=01),
         datetime(year=2017, month=05, day=01),
         datetime(year=2017, month=06, day=01),
         datetime(year=2017, month=07, day=01),
        ]

    timeseries_plot = TimeSeries(
        height='800px',
        width='500px',
        engine='highcharts',
        title='Irregular Timeseries Plot',
        y_axis_title='Snow depth',
        y_axis_units='m',
        series=[{
            'name': 'Winter 2007-2008',
            'data': [
                [datetime(2017, 12, 2), 0.8],
                [datetime(2017, 12, 9), 0.6],
                [datetime(2017, 12, 16), 0.6],
                [datetime(2017, 12, 28), 0.67],
                [datetime(2017, 1, 1), 0.81],
                [datetime(2017, 1, 8), 0.78],
                [datetime(2017, 1, 12), 0.98],
                [datetime(2017, 1, 27), 1.84],
                [datetime(2017, 2, 10), 1.80],
                [datetime(2017, 2, 18), 1.80],
                [datetime(2017, 2, 24), 1.92],
                [datetime(2017, 3, 4), 2.49],
                [datetime(2017, 3, 11), 2.79],
                [datetime(2017, 3, 15), 2.73],
                [datetime(2017, 3, 25), 2.61],
                [datetime(2017, 4, 2), 2.76],
                [datetime(2017, 4, 6), 2.82],
                [datetime(2017, 4, 13), 2.8],
                [datetime(2017, 5, 3), 2.1],
                [datetime(2017, 5, 26), 1.1],
                [datetime(2017, 6, 9), 0.25],
                [datetime(2017, 6, 12), 0]
            ]
        }]
    )

    my_plotly_view = PlotlyView([go.Scatter(x=x, y=[12, 14, 15, 10, 6, 5, 4])])

    context = {
        'select_input': select_input,
        'plotly_view_input': my_plotly_view,
        'timeseries_plot': timeseries_plot
    }

    return render(request, 'mysnowpackapp/mapview.html', context)


def dataservices(request):
    context = {

    }

    return render(request, 'mysnowpackapp/dataservices.html', context)


def about(request):
    context = {

    }

    return render(request, 'mysnowpackapp/about.html', context)

def proposal(request):
    context = {

    }

    return render(request, 'mysnowpackapp/proposal.html', context)

def mockups(request):
    context = {

    }

    return render(request, 'mysnowpackapp/mockups.html', context)

def addregions(request):

    text_input = TextInput(display_text='Add a Region',
                           name='inputAmount',
                           placeholder='e.g.: Sanpete County',
                           prepend='$')

    add_button = Button(
        display_text='Add',
        name='add-button',
        icon='glyphicon glyphicon-plus',
        style='info',
        attributes={
            'data-toggle': 'tooltip',
            'data-placement': 'top',
            'title': 'Add'}
    )

    context = {
        'text_input': text_input,
        'add_button': add_button,
    }

    return render(request, 'mysnowpackapp/addregions.html', context)
