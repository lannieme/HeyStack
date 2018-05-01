
import MySQLdb

DB_NAME  = 'HeyStack'
USERNAME = 'root'
PASSWORD = 'password'

def construct_SQL_query(input_data, c):
	# convert nouns to columns of interest

	cols_to_find = [input_data[0][0], input_data[2], input_data[4]]
	for i, search_col in enumerate(cols_to_find):
		q = ('select column_name' 
			 'from information_schema.columns' 
			 'where column_name like ' + ('\''+search_col+'\'')
			)
		tablecollist = execute_query(c, q)
		cols_to_find[i] = tablecollist[0]
	input_data[0][0] = cols_to_find[0]
	input_data[2]    = cols_to_find[1]
	input_data[4]    = cols_to_find[2]

	# search through tables for these columns
	potential_tables = dict()
	for potential_column in input_data:
		# find similar columns and their tables
		q = ('select table_name, column_name' 
			 'from information_schema.columns' 
			 'where column_name like ' + ('\''+potential_column+'\'')
			)
		tablecollist = execute_query(c, q) 
		# add each similar column and it's table to our data store
		for table, col in tablecollist:
			if table not in potential_tables:
				potential_tables[table] = set()
			potential_tables[table].add(col)

	# find likely table by getting table that satisfies all of the input desires
	lengths_dict = {table: len(s) for table, s in potential_tables.items()} # find number of hits in each table
	max_table = [table for table, set_length in lengths_dict.items() if set_length == max(lengths_dict.values())] # get table with most hits 

	# replace nouns in input with column names
	d = str.split(input_data[3][0])
	input_data[3] = ' '.join([d[0],'\''+d[1]+'\'', '\''+d[2]+'\'', d[3]])

	# find table with column_names


	# construct query	
	SQL_query = 'SELECT '+input_data[0][0]+', '+input_data[0][1]+' AS A FROM '+'Purchases'+' WHERE '+'date_of_purchase'+' '+input_data[3][0]+' GROUP BY '+input_data[4][0]+' ORDER BY A '+input_data[5][0]
	# SQL_query = 'SELECT State, SUM(purchase_amount) as A FROM Purchases where date_of_purchase between \'2017-02-01\' and \'2017-02-28\' group by state order by A DESC';
	# SQL_query = 'SELECT '+input_data[0][0]+', '+input_data[0][1]+' AS A FROM '+max_table[0]+' WHERE '+input_data[2]+' '+input_data[3]+' GROUP BY '+input_data[4]+' ORDER BY '+input_data[5]
	return SQL_query


def get_db_handle(db_name, username, password):
	db = MySQLdb.connect(passwd=password, db=db_name, user=username)
	c = db.cursor()
	return c

def execute_query (cursor, query_to_execute):
	cursor.execute(query_to_execute)
	query_output = cursor.fetchall()
	return query_output

def translation(select_words, time_strings, from_words, where_words, groupby_words, orderby_words):
	## transform input data

	# compile search_words
	search_words = set()
	for word in select_words:
		if word[:3].upper() == 'SUM':
			word = word[3:].strip('(').strip(')')
		search_words.add(word)
	for word in where_words:
		search_words.add(word)
	for word in groupby_words:
		search_words.add(word)

	input_data = [select_words, search_words, where_words, time_strings, groupby_words, orderby_words]
	c = get_db_handle(DB_NAME,USERNAME,PASSWORD)
	main_query = construct_SQL_query(input_data, c)
	results = execute_query(c, main_query)
	results = [ (row[0], float(row[1])  )for row in results]
	return main_query, results


if __name__ == '__main__':
	main_query, results = translation(['state','sum(purchase_amount)'], ['BETWEEN \'2017-02-01\' AND \'2017-02-28\''], [], ['date'], ['state'], ['DESC'])
	print('\nGenerated Query: \n\t', main_query)
	print('\nResults: \n\t', results)
	print()



