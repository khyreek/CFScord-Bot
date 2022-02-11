from webdriver_manager.chrome import ChromeDriverManager#type:ignore
from selenium.webdriver.chrome.service import Service#type:ignore
from selenium import webdriver#type:ignore

my_opts = webdriver.ChromeOptions()
my_opts.headless = True
my_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=my_service, options=my_opts)