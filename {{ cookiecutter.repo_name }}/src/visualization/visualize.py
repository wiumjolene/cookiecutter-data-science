import logging
import plotly.graph_objects as go
import pandas as pd
import numpy as np

from src.utils import colours


class VizScatter:
    logger = logging.getLogger(f"{__name__}.VizScatter")
    """
    https://plotly.com/python-api-reference/generated/plotly.graph_objects.Scatter.html
    https://plotly.com/python/line-and-scatter/
    """

    def scatterplot(self, data, metadata):
        """ 
        data = {'xaxes': [[x,x,x,x,x],[x,x,x,x,x],[x,x,x,x,x],[x,x,x,x,x]],
                'yaxes': [[y,y,y,y,y],[y,y,y,y,y],[y,y,y,y,y],[y,y,y,y,y]],
                'names': ['name','name','name','name'],
                'modes': [mode,mode,mode,mode],
                'colours': [colour,colour,colour,colour]
        }
        metadata = {
            'yaxis':{'name':'name', 'uom':'uom'},
            'xaxis':{'name':'name', 'uom':'uom'},
            'heading':'heading',
            'popcount':'popcount',
            'mode':'mode'
        }    
        """
        self.logger.debug(f"- scatterplot")

        fig = go.Figure()

        # Add traces
        for count, vals in enumerate(data['names']):

            fig.add_trace(go.Scatter(x=data['xaxes'][count], 
                                        y=data['yaxes'][count],
                                        mode=data['modes'][count],
                                        name=vals,
                                        marker_color=colours.COLOURS[data['colours'][count]])
                        )

        fig.update_traces(marker_line_width=0.3, marker_size=10)

        fig.update_layout(
            title=go.layout.Title(
                text=f"{metadata['heading']}<br><sup><i>(n={metadata['popcount']})</i></sup>",
                xref="paper",
                x=0
            ),
            xaxis=go.layout.XAxis(
                title=go.layout.xaxis.Title(
                    text=f"{metadata['xaxis']['name']}<br><sup><i>{metadata['xaxis']['uom']}</i></sup>"
                )
            ),
            yaxis=go.layout.YAxis(
                title=go.layout.yaxis.Title(
                    text=f"{metadata['yaxis']['name']}<br><sup><i>{metadata['yaxis']['uom']}</i></sup>"
                ),
                gridcolor=colours.GRIDCOLOUR
            ),
            paper_bgcolor = colours.PAPERBACKGROUND,
            plot_bgcolor=colours.PLOTBACKGROUND,
        )
        fig.show()
 