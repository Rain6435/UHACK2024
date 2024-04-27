# UHACK 2024

## User interface Mobile

- [ ] Team Login page pour team
- [ ] "Make a request" page
- [ ] Manager dashboard
- [ ] Team dashboard
- [ ] Track request

## Algorithme

- [ ] Define Data schema
	- [ ] Admin
		- Create any entity including admin
	- [ ] Request schema
		- [ ] Identify and extract relevant data from `VOIE_PUBLIQUE.csv`
	- [ ] Team schema
- [ ] Use data schemas to create test data
- [ ] Produce Pot-hole priority calculator algorithme
- [ ] Bonus: produce pot-hole shortest path algorithme

## Entities

- Team (or Admin)
	- Data
		- `id`, `name`, `password`, `work_time`, `work_season`, `secteur`, `is_admin`
	- Requirements
		- Team (`is_admin == 0`)
			- Actions
				- Can GET their own team data
				- Can GET their own assigned Requests
				- Can PUT their own assigned Request status
			- View
				- Team dashboard
		- Admin (`is_admin == 1`)
			- Actions
				- Can POST any entity
				- Can GET any/all entity
					- Include data agregation for request pending
				- Can PUT any entity
				- Can DELETE any entity
			- Views
				- View all/any team
				- View unified team dashboard
- Requestor
	- Data
		- `id`, `firstname`, `lastname`, `adresse`, `email`, `tel`
	- Requirements
		- Actions
			- can GET own data
			- Can PUT own data
			- can POST a request login
			- can Login with three different ways
				- Telephone (Optionnel ssi Firstname, lastname, adresse)
			- BONUS: receive updates about their request (if email is present)
	- Disclaimer
		- a requestor does NOT need to login to make a request. In fact, their is no login functionnality for the requestor.
- Request
	- Data
		- `id`, `location_id`, `team_id`, `requestor_id`, `is_dangerous`, `number_of_pothole`, `creation_date`, `lead_time`, `fix_date`, `status`, `image_path (as a bonus)`
	- Description
		- `lead_time`: the estimated time for the request to to be completed
		- `location_id`: this field is linked to the CODEID field of the Location table. To link, we need to extract the the street name and find inside the Location table the corresponding CODEID. So the location_id is linked to the CODEID. 
	- Disclaimer
		- We will not store the data of the user that made the request that resulted in the Request (See [UHACK2024 (Diapo 7)](https://www.peso-outaouais.ca/wp-content/uploads/2024/04/Case-Study.pdf))
		- The image path will be done as a bonus if we ever want to do image analysis
- Location
	- Data
		- "Use data from the `VOIE_PUBLIQUE.csv`"
	- Disclaimer
		- The `pk` will be the `CODEID` field
