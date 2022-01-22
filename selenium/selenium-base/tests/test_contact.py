from unittest.mock import Base
from seleniumbase import BaseCase

class ContactTest(BaseCase):
  
  def test_contact_page(self):
    siteUrl = "https://practice.automationbro.com/contact"
    self.open(siteUrl)
    
    self.send_keys('.contact-name input', 'Test Name')
    self.send_keys('.contact-email input', 'test@mail.com')
    self.send_keys('.contact-phone input', '123456789')
    self.send_keys('.contact-message textarea', 'This ia test message')
    
    self.click("#evf-submit-277")
    
    self.assert_text("Thanks for contacting us! We will be in touch with you shortly", "div[role=alert]")