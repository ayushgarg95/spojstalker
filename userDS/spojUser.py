from units.Lang import Lang
from units.ProbPool import ProbPool
from units.Submission import Submission
from datetime import datetime, timedelta
from prob_info.models import ProblemClassical
import pickle
from bs4 import BeautifulSoup
import urllib2

class spojUser:
	"""
	Everything needed about the spoj user
	"""
	def __init__(self, name, user_name, rank, points, classical):
		self.name = name
		self.user_name = user_name
		self.rank = rank
		self.points = points
		self.classical = classical
		
		self.lang = Lang()
		self.probPool = ProbPool()
		self.submission = Submission()
		self.classical_table = {}
		self.latest_date = {}
		#self.latest_name = {}

	def merge_submission(self, date_of_sub, problem_id, sub_result, lng_sub):
		self.lang.update(lng_sub)
		self.submission.update(sub_result)
		self.probPool.update(problem_id, sub_result, date_of_sub)

	def classical_total(self):
		return len(self.classical)

	def get_classical_table(self):
		users_solved = pickle.loads(ProblemClassical.objects.all()[0].data)

		ret = {}
		points = {}
		for id in self.classical:
			res = '??'
			if self.probPool.main.has_key(id) and self.probPool.main[id].AC:
				days = (datetime.now()+timedelta(hours=2)-self.probPool.main[id].first_AC)
				res = str(days.days)
			xx = round( float(float(80) / ( float(users_solved.get(id, -1)) + float(40) )) , 3)
			ret[id] = (res+' days ago', str(xx))
			points[str(id)] = str(xx)
		self.classical_table = points

        def get_latest(self):
                url = "http://www.spoj.com/status/"+self.user_name+"/"
                content = urllib2.urlopen(url).read()
                users_solved = pickle.loads(ProblemClassical.objects.all()[0].data)
                soup = BeautifulSoup(content)

                count = 0
                ct = 0
                ret = {}
                for id1 in soup.find_all("table", attrs={"class" : "problems"}):
                        for id2 in id1.find_all("tr"):
                                if count>55:
                                        break
                                count = count +1

                                for time in id2.find_all("td",attrs={'class': 'status_sm'}):
                                        dat = time.get_text()
                                for status in id2.find_all("td",attrs={'class': 'statusres text-center'}):
                                        acc = status.get_text()
                                for id in id2.find_all("a"):
                                        name = id.get('title')
                                        if name!="See the best solutions" and name !='None':
                                                xx = round( float(float(80) / ( float(users_solved.get(name,1000000)) + float(40) )) , 3)
                                                ret[ct] = (str(name), id.get_text(), str(xx), str(acc), str(dat))
                                                ct += 1
                self.latest_date = ret


                
                
