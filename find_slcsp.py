import csv

# Load the zips from slcsp.csv
with open('slcsp.csv', 'rt') as slcsp:
    q_ziplist = csv.reader(slcsp)
    zip_dict = {}
    # For each zip loaded
    for qzip in q_ziplist:
        # Add the zip to a dictionary with the zip as the primary key
        if qzip[0] not in zip_dict:
            zip_dict[qzip[0]] = ''
        else:
            print("Duplicate zip in q_ziplist")

# Load the zips.csv
with open('zips.csv', 'rt') as zipfile:
    zipdata = csv.reader(zipfile)
        # search the zips.csv file for all entries with that zip
    for key in zip_dict:
        matches = []
        # when make a list of rows that have the qzip
        for row in zipdata:
            print("row[0] =")
            print(row[0])
            print("row =")
            print(row)
            print("key =")
            print(key)
            if row[0] == key:
                matches.append(row)
                print('matches')
                print(matches)
            # if no qzips found in zip file, print the issue
            if len(matches) == 0:
                print("Zip is not in zipsfile")
            # if there's only one match, no more processing necessary
            elif len(matches) == 1:
                zip_dict[key] = row
                print('the row is')
                print('dict_key is')
                print(zip_dict[key])
                zip_dict[key].append(0)
            # if multiple zips found, need to test if the rate areas are the same
            elif len(matches) > 1:
                firstMatch = matches[0]
                firstRateArea = (firstMatch[1], firstMatch[4])
                for row in matches:
                    rate_area = (row[1], row[4])
                    # if rate_area is not the same, cannot determine slcsp, return empty quotes
                    if rate_area != firstRateArea:
                        zip_dict[key].append('')
                        break
                # if all matches have the same rate_area, we'll calculate the slcsp in the next section
                if len(zip_dict[key]) < 5:
                    zip_dict[key].append(0)

print(zip_dict)
        # if zips have multiple rate areas, save slcsp as blank
        # if zip is found in with multiple county codes
            # if all rate areas are equal, then calc slcsp
            # if multiple rate areas in zip, save slcsp as blank

# Calculating slcsp
    # find the available plans in the state and rate area, load the silver plans
        #       exceptions - can't find zip in zips dictionary, state/rate area
        #       not listed in plans.csv, no silver plans
    # rank all plans found by rate
    # find the second lowest plan
        #       robustness - second lowest plan ignores low duplicates
    # write rate to csv in format zip, rate (#####, ###.##)


# ensure proper std_out output
