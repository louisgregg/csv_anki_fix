import csv
import sys

replacement_word_list = {
'i ':'yo ',
'you ':'tú ',
'he/she':'él/ella/Ud. ',
'we ':'nosotros ',
'you_plural_dummy ':'vosotros ',
'they ':'ellos/ellas/Uds. '
}

def import_stuff_and_wrangle(filenames):
	print(filenames[1])
	with open(filenames[1]) as csv_file:
		csv_read=csv.reader(csv_file,delimiter='\t')
		csv_as_list = list(csv_read)
		return(csv_as_list)

def fix_rows(list_of_rows):
	for row in list_of_rows:
		row=row_logic(row)
	return(list_of_rows)

def row_logic(old_row):
	try:
		old_row[0]=old_row[0].lower().replace('you (pl)','you_plural_dummy')
		old_row[1]=old_row[1].lower().replace('you (pl)','you_plural_dummy')
		
	except AttributeError as e:
		pass
	

	for key, value in replacement_word_list.items():
		if key in old_row[0].lower():
			old_row[1]=value+old_row[1]
		if key in old_row[1].lower():
			old_row[0]=value+old_row[0]
	
	try:
		old_row[0]=old_row[0].lower().replace('you_plural_dummy','you (pl)')
		old_row[1]=old_row[1].lower().replace('you_plural_dummy','you (pl)')
		
	except AttributeError as e:
		pass			

	print(old_row)		
	return(old_row)

def export_list_to_csv(fixed_list_of_rows,filenames):
	output_filename=filenames[1]+'_fixed.txt'

	with open(output_filename, 'w', newline='') as csvfile:
		writer_object = csv.writer(csvfile, delimiter='	',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
		for row in fixed_list_of_rows:
			writer_object.writerow(row)

if __name__ == '__main__':
	list_of_rows=import_stuff_and_wrangle(sys.argv)
	fixed_list_of_rows=fix_rows(list_of_rows)
	export_list_to_csv(fixed_list_of_rows,sys.argv)