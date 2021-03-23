counties = ["Arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")
if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list.")

for county in counties:
    print(county)


for num in range(5):
    print(num)

for i in range(len(counties)):
    print(counties[i])

for county in counties_dict:
    print(county)

#
# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
#
# On branch main
# Your branch is up to date with 'origin/main'.
#
# Changes to be committed:
#	new file:   Resources/2017 Refactored.png
#	new file:   Resources/2017_before_refactor.png
#	new file:   Resources/2018 Refactored.png
#	new file:   Resources/2018_before_refactor.png
#
# Changes not staged for commit:
#	modified:   green_stocks.xlsm
#
# Untracked files:
#	.DS_Store
#
