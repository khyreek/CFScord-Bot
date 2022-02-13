from bs4 import BeautifulSoup#type:ignore
from urllib.request import urlopen
import cv2 as cv#type:ignore
from typing import Generator
import numpy as np
import random

from assisters.myconsts import CFS_ENTIRE_PROBLEM_FILENAME, CFS_LETTER_CODES, MAXIMUM_CFS_CROP_HEIGHT, TAG_OPTIONS
from toolkit import cfs_problem_info, cfs_hashtag
from assisters.mytypes import Problem

def cfs_combiner(
		problem: Problem
	) -> Generator[np.ndarray, None, None]:
	"""
	this function goes through every y location of the sections (given by data)
	and attempts to make the least crops by looking at the section starting locations 
	from the back and checking if they are less than a heigh threshold (600 currently),

	yield the cropping

	if the distance between consecutive sections is already greater than the threshold,
	just yield that section as a crop
	"""
	
	problem_width, locations_data = cfs_problem_info(problem)
	full_problem = cv.imread(CFS_ENTIRE_PROBLEM_FILENAME)

	while locations_data:
		if len(locations_data) == 1:
			# here, the last item in locations_data is the footer, 
			# nothing comes after this so the loop would go infinite
			break

		for i in range(1, len(locations_data)):
			"""
			this is the main loop, it indexes from the back of the locations data looking for
			enough distance between the y locations to make a cropping (this will thus get the
			least amount of croppings))
			
			(for loop starts from 1 cause slicing below would be pointless
			not adding 1 to upper bound cause then indexing would be useless by last iteration)

			the guard checks the distance between the currently pointed-towards y locations
			and checks if they have a height low enough to be cropped as a portion
			
			however, this would be an infinite while loop if two consecutive sections
			already had too much height to be cropped, and so a guard is made for that

			finally the locations data storage of y locations is updated to remove the cropped 
			section for the next iteration to recurse properly 
			"""
			if (first_guard := locations_data[-i] - locations_data[0] < MAXIMUM_CFS_CROP_HEIGHT) or (
					not first_guard and i == (len(locations_data) - 1)
				):
				yield full_problem[
					locations_data[0] : locations_data[-i],
					0 				  : problem_width
				]
				
				locations_data = locations_data[-i :]
				break

def random_cfs() -> Problem:
	"""
	.
	"""
	
	range_site = "https://codeforces.com/problemset"
	range_html = urlopen(range_site).read().decode('utf-8')
	range_soup = BeautifulSoup(range_html, 'html.parser')
	page_range = int(
		range_soup
			.find_all('span', class_='page-index')
			[-1]
			['pageindex']
	)

	probs_site = f'{range_site}/page/{random.randrange(page_range)}'
	
	return cfs_hashtag(probs_site)
	
def filter_cfs(min_rating: int, max_rating: int, filters: tuple[str, ...]) -> Problem:
	"""
	pas
	"""

	if filters: assert not all(t not in TAG_OPTIONS for t in TAG_OPTIONS), 'None if your tag filters were valid'

	genre_filter = "https://codeforces.com/problemset?tags=" + (
		''.join(
			filter + ',' if filter in ('meet-in-the-middle', '2-sat', 'combine-tags-by-or') else
			filter.replace('-', '%20') + ','
			for filter in filters
		)
	)
	# print(f"{genre_filter}{min_rating}-{max_rating}")
	return cfs_hashtag(f"{genre_filter}{min_rating}-{max_rating}")
	
def submit_cfs(problem: Problem):
	letter_code = [char for char in problem if char in CFS_LETTER_CODES][0]
	split = problem.index(letter_code)
	link_addon = problem[: split] + '/' + problem[split: ]
	return "https://codeforces.com/problemset/problem/" + link_addon + "#:~:text=%C2%A0-,%E2%86%92%20Submit%3F,-Language%3A"


# if __name__ == "__main__":
	# print(filter_cfs(1, 2000, ('binary-search', )))
