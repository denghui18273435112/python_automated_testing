import requests,json
from test_data.SongQin_Variable import *
from pprint import pprint
from  robot.libraries.BuiltIn import BuiltIn
#from openpyxl import load_workbook

class SongQin_API:
	def __init__(self):
		self.vcode = g_vcode
		self.URL = g_URL
		self.student_URL = student_URL
		self.teacher_URL = teacher_URL

	# 列出班级
	def list_school_class(self, gradeid=None):
		if gradeid != None:
			params = {
				"vcode": self.vcode,
				"action": "list_classes_by_schoolgrade",
				"gradeid": int(gradeid)
			}
		else:
			params = {
				"vcode": self.vcode,
				"action": "list_classes_by_schoolgrade"
			}
		# 列出班级的请求参数是在url里；url对应get方法中的参数：params参数
		# get；#url 请求url；params是请求参数；headers是请求头;data是消息体参数
		response = requests.get(url=self.URL, params=params)
		bodyDict = response.json()  # json的字符串转换成python的服务对象；为什么换成？转换python中的对象，目的方便分析；
		pprint(bodyDict, indent=2)  # 漂亮的打印，indent=2 表示缩进的空格数
		return bodyDict

	def list_school_class_1(self, idSavedName=None):
		if gradeid != None:
			params = {
				"vcode": self.vcode,
				"action": "list_classes_by_schoolgrade",
				"gradeid": int(gradeid)
			}
		else:
			params = {
				"vcode": self.vcode,
				"action": "list_classes_by_schoolgrade"
			}
		# 列出班级的请求参数是在url里；url对应get方法中的参数：params参数
		# get；#url 请求url；params是请求参数；headers是请求头;data是消息体参数
		response = requests.get(url=self.URL, params=params)
		bodyDict = response.json()  # json的字符串转换成python的服务对象；为什么换成？转换python中的对象，目的方便分析；
		pprint(bodyDict, indent=2)  # 漂亮的打印，indent=2 表示缩进的空格数

		if idSavedName:
			BuiltIn().set_global_variable("${%s}" % idSavedName, bodyDict["retlist"][0]["id"])
		return bodyDict

	# 添加班级
	def add_school_class(self, gradeid, name, studentlimit,
	                     idSavedName=None):
		data = {
			"vcode": self.vcode,
			"action": "add",
			"grade": int(gradeid),
			"name": name,
			"studentlimit": int(studentlimit)
		}

		# 添加班级的请求参数是在请求体内容里；请求体内容对应post方法中的参数：data参数
		response = requests.post(self.URL, data=data)
		bodyDict = response.json()  # 转换成python对象
		pprint(bodyDict, indent=2)  # 漂亮的打印，indent=2 表示缩进的空格数

		if idSavedName:
			BuiltIn().set_global_variable("${%s}" % idSavedName, bodyDict["id"])
		return bodyDict

	# 返回
	def fanhui(self, neirong):

		return neirong

	# 修改班级
	def modify_school_class(self, classid, NewName, NenStudentlimit):
		data = {
			"vcode": self.vcode,
			"action": "modify",
			"name": NewName,
			"studentlimit": int(NenStudentlimit)
		}

		url = "{}/{}".format(self.URL, classid)  # 拼接字符串
		# 添加班级的请求参数是在请求体内容里；请求体内容对应post方法中的参数：data参数
		response = requests.put(url, data=data)
		bodyDict = response.json()  # 转换成python对象
		pprint(bodyDict, indent=2)  # 漂亮的打印，indent=2 表示缩进的空格数
		return bodyDict

	# 删除班级
	def delete_school_calss(self, classid):
		payload = {
			"vcode": self.vcode
		}
		# /ci.ytesting.com/api/3school/school_classes/<classid>   ;不是？后面的参数，需要拼接的；就是一个url
		url = "{}/{}".format(self.URL, classid)
		response = requests.delete(url, data=payload)
		return response.json()

	# 删除所有班级
	def delete_all_school_calsses(self):
		# 先列出所有班级
		rd = self.list_school_class()
		pprint(rd, indent=2)

		# 删除列出的所有班级
		for one in rd["retlist"]:
			self.delete_school_calss(one["id"])
		# 在列出所有班级
		rd = self.list_school_class()
		pprint(rd, indent=2)

		# if rd["retlist"] != []:
		# 	raise Exception("cannot delete all school calsses!!")

	# 班级的比较；添加的班级有没有在班级列表中
	def classlist_should_contain(self, classlist,
	                             gradename, classid, invitecode, classname, studentlimit, studentnumber,
	                             expectedtimes=1):

		item = {
			"grade__name": gradename,  # 年级
			"id": classid,  # 班级id
			"invitecode": invitecode,  # invitecode
			"name": classname,  # 班级名称
			"studentlimit": int(studentlimit),  # 班级的上限人数
			"studentnumber": int(studentnumber),  # 班级现有人数
			"teacherlist": []
		}

		# 比较 如果有包含，则会返回1
		occurTimes = classlist.count(item)

		if occurTimes != expectedtimes:
			# 抛出异常，在rf就表示不通过
			raise Exception('班级列表包含了%{occurTimes}次制定信息，期望包含%{expectedtimes}！！')


		# 列出老师
	def list_teacher(self, subjectid=None):
		params = {
			"vcode": self.vcode,
			"action": "search_with_pagenation"
		}
		if subjectid != None:
			params["subjectid"] = int(subjectid)

		# 列出班级的请求参数是在url里；url对应get方法中的参数：params参数
		# get；#url 请求url；params是请求参数；headers是请求头;data是消息体参数
		response = requests.get(url=teacher_URL, params=params)
		bodyDict = response.json()  # json的字符串转换成python的服务对象；为什么换成？转换python中的对象，目的方便分析；
		pprint(bodyDict, indent=2)  # 漂亮的打印，indent=2 表示缩进的空格数
		return bodyDict

	# 添加老师
	def add_teacher(self, username, realname, subjectid, classlist, phonenumber, email, idcardnumber,
	                idSavedName=None):
		# 列表生成试
		classlist=str(classlist)
		newClassList = [{"id":oneid} for oneid in classlist.split(",") if oneid]
		#newClassList = [{"id": classlist}]

		data = {
			"vcode": self.vcode,
			"action": "add",
			"username": username,
			"realname": realname,
			"subjectid": int(subjectid),
			"phonenumber": int(phonenumber),
			"email": email,
			"idcardnumber": idcardnumber,
			"classlist":json.dumps(newClassList)  # 转换成字符串
			#"classlist": newClassList
		}
		response = requests.post(url=self.teacher_URL, data=data)
		bodyDict = response.json()
		pprint(bodyDict, indent=2)
		#存放全局变量
		if idSavedName:
			BuiltIn().set_global_variable("${%s}" % idSavedName, bodyDict["id"])
		return bodyDict

	# 修改老师
	def modify_teacher(self, teacherid, realname=None,
	                   subjectid=None, classlist=None,
	                   phonenumber=None, email=None, idcardnumber=None):

		data = {
			"vcode": self.vcode,
			"action": "add",
		}

		if realname != None:
			data["realname"] = realname
		if subjectid != None:
			data["subjectid"] = subjectid
		if phonenumber != None:
			data["phonenumber"] = phonenumber
		if email != None:
			data["email"] = email
		if idcardnumber != None:
			data["idcardnumber"] = idcardnumber
		if classlist != None:
			# 列表生成试
			classlist = str(classlist)
			newClassList = [{"id": oneid} for oneid in classlist.split(",") if oneid]
			data["classlist"] = json.dumps(newClassList)  # 转换成字符串

		# 添加班级的请求参数是在请求体内容里；请求体内容对应post方法中的参数：data参数

		url = "{}/{}".format(teacher_URL, teacherid)
		response = requests.put(url, data=data)
		bodyDict = response.json()  # 转换成python对象
		pprint(bodyDict, indent=2)  # 漂亮的打印，indent=2 表示缩进的空格数

		return bodyDict

	# 删除老师
	def delete_teacher(self, tahcerid):
		payload = {
			"vcode": self.vcode
		}
		# /ci.ytesting.com/api/3school/school_classes/<classid>   ;不是？后面的参数，需要拼接的；就是一个url
		url = "{}/{}".format(teacher_URL, tahcerid)
		response = requests.delete(url, data=payload)
		return response.json()

	# 删除所有老师
	def delete_all_teacher(self):
		# 先列出所有老师
		rd = self.list_teacher()
		pprint(rd, indent=2)

		# 删除所有老师
		for one in rd["retlist"]:
			self.delete_teacher(one["id"])

		# 在列出所有老师
		rd = self.list_teacher()
		pprint(rd, indent=2)

		# 如果没有删除干净，通过异常报错给rf
		if rd["retlist"] != []:
			raise Exception("cannot delete all teacher!!")


		#  老师的比较学习到这里

	def teacher_list_should_contain(self, teacherList, realname, subjectid, classlist, phonenumber, email, idcardnumber,
	                                expectedtimes=1):

		item = {
			"name": classname,  # 班级名称
			"grade__name": gradename,  # 年级
			"invitecode": invitecode,  # invitecode
			"studentlimit": int(studentlimit),  # 班级的上限人数
			"studentnumber": int(studentnumber),  # 班级现有人数
			"id": classid,  # 班级id
			"teacherlist": []
		}
		occurTimes = classlist.count(item)
		print("occur {} times".format(occurTimes))

		if occurTimes != expectedtimes:
			# 抛出异常，在rf就表示不通过
			raise Exception('班级列表包含了%{occurTimes}次制定信息，期望包含%{expectedtimes}！！')

	# 列出学生
	def list_student(self):
		params = {
			"vcode": self.vcode,
			"action": "search_with_pagenation"
		}
		# 列出班级的请求参数是在url里；url对应get方法中的参数：params参数
		# get；#url 请求url；params是请求参数；headers是请求头;data是消息体参数
		response = requests.get(url=self.student_url, params=params)
		bodyDict = response.json()  # json的字符串转换成python的服务对象；为什么换成？转换python中的对象，目的方便分析；
		pprint(bodyDict, indent=2)  # 漂亮的打印，indent=2 表示缩进的空格数
		return bodyDict

	# 添加学生
	def add_student(self, username, realname, gradeid, classid, phonenumber,
	                idSavedName=None, scope="global"):
		data = {
			"vcode": self.vcode,
			"action": "add",
			"username": username,
			"realname": realname,
			"gradeid": gradeid,
			"classid": classid,
			"phonenumber": phonenumber
		}

		# 添加班级的请求参数是在请求体内容里；请求体内容对应post方法中的参数：data参数
		response = requests.post(self.student_URL, data=data)
		bodyDict = response.json()  # 转换成python对象
		pprint(bodyDict, indent=2)  # 漂亮的打印，indent=2 表示缩进的空格数

		# 设置全局变量
		if idSavedName:
			if scope == "global":
				BuiltIn().set_global_variable("${%s}" % idSavedName, bodyDict["id"])
			if scope == "suite":
				BuiltIn().set_suite_variable("${%s}" % idSavedName, bodyDict["id"])
			if scope == "case":
				BuiltIn().set_case_variable("${%s}" % idSavedName, bodyDict["id"])
		return bodyDict

		# if idSavedName:
		# 	BuiltIn().set_global_variable("${%s}" % idSavedName, bodyDict["id"])
		# return bodyDict
	# 修改学生
	def modify_student(self, studentid, realname=None, phonenumber=None):
		data = {
			"vcode": self.vcode,
			"action": "modify",
		}

		if realname != None:
			data["realname"] = realname
		if phonenumber != None:
			data["phonenumber"] = phonenumber

		url = "{}/{}".format(self.student_URL, studentid)
		response = requests.put(url, data=data)
		bodyDict = response.json()
		pprint(bodyDict, indent=2)
		return bodyDict

	# 删除学生
	def delete_student(self, studentid):
		payload = {
			"vcode": self.vcode
		}
		# /ci.ytesting.com/api/3school/school_classes/<classid>   ;不是？后面的参数，需要拼接的；就是一个url
		url = "{}/{}".format(self.student_URL, studentid)
		response = requests.delete(url, data=payload)
		return response.json()

	# 删除所有学生
	def delete_all_student(self):
		# 先列出所有学生
		rd = self.list_student()
		pprint(rd, indent=2)

		# 删除所有学生
		for one in rd["retlist"]:
			self.delete_student(one["id"])

		# 在列出所有学生
		rd = self.list_student()
		pprint(rd, indent=2)

		# 如果没有删除干净，通过异常报错给rf
		if rd["retlist"] != []:
			raise Exception("cannot delete all teacher!!")


		#  学生的比较
	def student_list_should_contain(self, studentList, username, realname, phonenumber, studentid, classid,
	                                expectedtimes=1):

		item = {
			"username": username,
			"realname": realname,
			"phonenumber": phonenumber,
			"id": int(studentid),
			"classid": int(classid)
		}

		occurTimes = studentlist.count(item)  # 查看包含多少次
		print("occur {} times".format(occurTimes))

		if occurTimes != expectedtimes:
			# 抛出异常，在rf就表示不通过
			raise Exception('学生列表包含了%{occurTimes}次制定信息，期望包含%{expectedtimes}！！')

	# 年级编号转换成对应的值
	def grade_number_conversion_value(self, grade_id):

		if grade_id == 1:
			return "七年级"
		elif grade_id == 2:
			return "八年级"
		elif grade_id == 3:
			return "九年级"
		elif grade_id == 4:
			return "高一"
		elif grade_id == 5:
			return "高二"
		elif grade_id == 6:
			return "高三"

		# 年级值转换成编号

	def grade_values_converted_nubers(self, grade_value):

		if grade_value == "七年级":
			return 1
		elif grade_value == "八年级":
			return 2
		elif grade_value == "九年级":
			return 3
		elif grade_value == "高一":
			return 4
		elif grade_value == "高二":
			return 5
		elif grade_value == "高三":
			return 6

		# 科目编号转换成对应的值
	def subject_number_conversion_value(self, subject_id):
		if subject_id == 1:
			return "1"  # 初中数学
		elif subject_id == 5:
			return "5"  # 初中科学
		elif subject_id == 11:
			return "11"  # 初中英语
		elif subject_id == 12:
			return "12"  # 初中体育
		elif subject_id == 13:
			return "13"  # 高中语文
		elif subject_id == 14:
			return "14"  # 高中数学

	# 未执行代码的方法
	def Unexecuted_code(self):
		pass_vules = "未执行任何代码"
		return pass_vules

	# 列出学生
	def list_student(self):
		params = {
			"vcode": self.vcode,
			"action": "search_with_pagenation"
		}
		# 列出班级的请求参数是在url里；url对应get方法中的参数：params参数
		# get；#url 请求url；params是请求参数；headers是请求头;data是消息体参数
		response = requests.get(url=self.student_URL, params=params)
		bodyDict = response.json()  # json的字符串转换成python的服务对象；为什么换成？转换python中的对象，目的方便分析；
		pprint(bodyDict, indent=2)  # 漂亮的打印，indent=2 表示缩进的空格数
		return bodyDict

	# 自定义断言  contrast_parameter;code 条件；case_name 测试名称
	def new_assert(self,contrast_parameter,code,case_name):
		if contrast_parameter==code:
			print("成功"+case_name)
		else:
			print(case_name+"失败")