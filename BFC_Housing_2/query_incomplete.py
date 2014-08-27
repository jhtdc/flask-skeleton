def query(Age_With_Disability=None, Age_Without_Disability=None, Bedrooms_Needed=None, Disability=None, HAP_End_Date=None,HAP_Start_Date=None,Mobility_Impairment=None, Status=None, RecordType_Name=None):
	




						
						
	base_query="""SELECT ID, Intake__r.FirstName__c, Intake__r.LastName__c, 
		Intake__r.PrimaryPhoneNo__c,Intake__r.PrimaryPhoneNoType__c
		FROM Case__c Where Intake__r.PrimaryPhoneNoType__c= 'Mobile'"""

	if Age_With_Disability is not None and Disability = TRUE:
		base_query+=' and (( Age__c >= ' + Age_With_Disability + ' and Disability__c = true )'
		if Age_Without_Disablity is not None
			base_query += ' OR ' 

	if Age_Without_Disability is not None
			base_query += '( Age__c >= ' + Age_Without_Disability + ' and Disability__c = false )'
		else 
			base_query += ')' 
	

	if Bedrooms_Needed is not None:
		base_query+=' and Bedrooms_Needed__c >= ' + Bedrooms_Needed

	if Disability is not None:
		base_query+=' ' 

	if HAP_Start_Date is not None:

	if HAP_End_Date is not None:

	if Mobility_Impairment is not None:

	if Status is not None:

	if RecordType_Name is not None:











	if Bedrooms_Needed__c is not= then base_query 
	if Disability__c is not=then base_query 
	if HAP_Start_Date__c is not=then base_query
	if HAP_End_Date__c is not=then base_query
	if Intake__c is not=then base_query
	if Mobility_Impairment__c is not=then base_query
	if Status __c is not=then base_query
	if RecordType_Name__c is not=then base_query



				


