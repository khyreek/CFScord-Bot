from bs4 import BeautifulSoup#type:ignore
from urllib.request import urlopen
import selenium#type:ignore
from typing import Literal
import random
import re

from assisters.myconsts import CFS_LETTER_CODES, CFS_PROBLEM_LINK_PREFIX, CFS_ENTIRE_PROBLEM_FILENAME
from assisters.mytypes import CFSSectionsData, Problem, ProblemWidth
from assisters.preparation import driver

def site_dimension(dim: Literal['Width', 'Height']) -> int:
	assert dim in ('Width', 'Height'), 'This command expects \'Width or \'Height'
	
	return driver.execute_script('return document.body.parentNode.scroll' + dim)

def cfs_problem_info(problem: Problem) -> tuple[ProblemWidth, CFSSectionsData]:
	"""
	save the problem page - to crop on with the sizes of the problem portions listed below;
		header info,
		description
			(no class in the html exists for this part, so customized data is made to 
			simulate an html element),
		sections of the problem 

	returns the width and a tuple of the y location on the website of the portions listed above
	the location's 'y' coordinate will be subtracted by the y location of where the problem started
	- this is so the croppings will have relative information
	"""

	try:
		problem = problem.upper()
		code_letter = [let for let in problem if let in CFS_LETTER_CODES] # get letter in problem code
		assert code_letter, "No problem letter code was given"

		split = problem.index(code_letter[0])
		link_addon = '/'.join((
			problem[: split], 
			problem[split :]
		))

		driver.get(CFS_PROBLEM_LINK_PREFIX + link_addon)
		driver.set_window_size(site_dimension('Width'), site_dimension('Height'))
		full_problem = driver.find_element('class name', value='problem-statement')
		full_problem.screenshot(CFS_ENTIRE_PROBLEM_FILENAME)

		problem_width = full_problem.size['width']
		start_offset = full_problem.location['y'] # top left location of where problem starts
		header = driver.find_element('class name', value='header')
		sections = driver.find_elements('class name', value='section-title')
		footer = driver.find_element('id', value='footer')

		return (
			problem_width, tuple(
				y_location - start_offset
				for y_location
				in (
					header.location['y'], # header
					header.location['y'] + header.size['height'], # description

					# sections and footer
					*(problem_portion.location['y'] for problem_portion in (*sections, footer))
				)
			)
		)

	except selenium.common.exceptions.NoSuchElementException:
		assert 0, "That CFS problem does not exist"

def cfs_hashtag(link: str):
	"""
	asd
	"""

	probs_html = urlopen(link).read().decode('utf-8')
	probs_soup = BeautifulSoup(probs_html, 'html.parser')
	
	top_level = probs_soup.find_all('tr')[1 : -1]
	bot_level = (
		prob
			.find_all('td')[0]
			.find_all('a')[0]
			['href']
		for prob
		in top_level
	)

	chosen_problem = random.choice(tuple(bot_level))
	return (
		re.findall('[1-9].*[A-K]', chosen_problem)[0]
			.replace('/', '')
	)

