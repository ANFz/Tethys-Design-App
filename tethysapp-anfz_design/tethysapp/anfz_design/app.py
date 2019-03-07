from tethys_sdk.base import TethysAppBase, url_map_maker


class AnfzDesign(TethysAppBase):
    """
    Tethys app class for Display App.
    """

    name = 'Display App'
    index = 'anfz_design:home'
    icon = 'anfz_design/images/perfection.jpg'
    package = 'anfz_design'
    root_url = 'anfz-design'
    color = '#000000'
    description = 'Showing our App design'
    tags = '&quot;Wireframe&quot;,&quot;Proposal&quot;'
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
                url='anfz-design',
                controller='anfz_design.controllers.home'
            ),
            UrlMap(
                name='proposal',
                url='proposal',
                controller='anfz_design.controllers.proposal'
            ),
            UrlMap(
                name='wireframe',
                url='wireframe',
                controller='anfz_design.controllers.wireframe'
            ),
        )

        return url_maps

