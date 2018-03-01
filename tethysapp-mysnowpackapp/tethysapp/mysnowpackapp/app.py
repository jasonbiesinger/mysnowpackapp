from tethys_sdk.base import TethysAppBase, url_map_maker


class Mysnowpackapp(TethysAppBase):
    """
    Tethys app class for Snowpack Viewer App.
    """

    name = 'Snowpack Viewer App'
    index = 'mysnowpackapp:home'
    icon = 'mysnowpackapp/images/cloudicon.png'
    package = 'mysnowpackapp'
    root_url = 'mysnowpackapp'
    color = '#ADD8E6'
    description = 'This app lets you see snowpack over Utah.'
    tags = '&quot;snowpack&quot;, &quot;utah&quot;, &quot;engineering&quot;, &quot;awesome&quot;'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)
        url_maps = (
            UrlMap(
                name='home',
                url='mysnowpackapp',
                controller='mysnowpackapp.controllers.home'
            ),
            UrlMap(
                name='mapview',
                url='mysnowpackapp/mapview',
                controller='mysnowpackapp.controllers.mapview'
            ),
            UrlMap(
                name='dataservices',
                url='mysnowpackapp/dataservices',
                controller='mysnowpackapp.controllers.dataservices'
            ),
            UrlMap(
                name='about',
                url='mysnowpackapp/about',
                controller='mysnowpackapp.controllers.about'
            ),
            UrlMap(
                name='proposal',
                url='mysnowpackapp/proposal',
                controller='mysnowpackapp.controllers.proposal'
            ),
            UrlMap(
                name='mockups',
                url='mysnowpackapp/mockups',
                controller='mysnowpackapp.controllers.mockups'
            ),
            UrlMap(
                name='addregions',
                url='mysnowpackapp/addregions',
                controller='mysnowpackapp.controllers.addregions'
            ),

        )

        return url_maps
