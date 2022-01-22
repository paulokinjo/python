from seleniumbase import BaseCase


class HomeTest(BaseCase):

    def test_home_page(self):
        siteUrl = "https://practice.automationbro.com/"
        self.open(siteUrl)

        self.assert_title("Practice E-Commerce Site – Automation Bro")

        self.assert_element(".custom-logo")

        self.assert_text("Think different. Make different.", "h1")

        self.scroll_to_bottom()

        self.assert_text("Copyright © 2020 ", ".tg-site-footer-section-1")

        get_started_link_id = "#get-started"
        self.click(get_started_link_id)
        get_started_url = self.get_current_url()
        self.assert_equal(get_started_url, siteUrl + get_started_link_id)
        self.assert_true(get_started_link_id in get_started_url)

    def test_menu_links(self):
        siteUrl = "https://practice.automationbro.com/"
        self.open(siteUrl)

        expected_links = ['Home', 'About', 'Shop',
                          'Blog', 'Contact', 'My account']
        
        menu_links = self.find_elements('//*[@id="primary-menu"]/*[starts-with(@id, "menu-item")]')
        for idx, link in enumerate(menu_links):
            self.assertEqual(expected_links[idx], link.text);
