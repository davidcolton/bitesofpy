from pathlib import Path
import csv
import json
from json.decoder import JSONDecodeError

EXCEPTION = "exception caught"
TMP = Path("/tmp")


def convert_to_csv(json_file):
    """Read/load the json_file (local file downloaded to /tmp) and
       convert/write it to defined csv_file.
        The json_data is in mounts > collected

       Catch bad JSON (JSONDecodeError) file content, in that case print the defined
       EXCEPTION string ('exception caught') to stdout reraising the exception.
       This is to make sure you actually caught this exception.

       Example csv output:
       creatureId,icon,isAquatic,isFlying,isGround,isJumping,itemId,name,qualityId,spellId
       32158,ability_mount_drake_blue,False,True,True,False,44178,Albino Drake,4,60025
       63502,ability_mount_hordescorpionamber,True,...
       ...
    """  # noqa E501
    csv_file = TMP / json_file.name.replace(".json", ".csv")

    # Placeholder for JSON
    json_data = ""

    with open(json_file) as input_file:
        # Read in the JSON
        try:
            json_data = json.load(input_file)
        # JSON Error, print exception and raise
        except JSONDecodeError:
            print(EXCEPTION)
            raise

    # Get the collected JSON data
    collected = json_data["mounts"]["collected"]

    # Use a csv DictWrite to writer to generate the output
    with open(csv_file, "w") as output_file:
        csv_writer = csv.DictWriter(
            output_file, fieldnames=sorted(list(collected[0].keys()))
        )

        # Write the header
        csv_writer.writeheader()

        # Write out the data
        for row in collected:
            csv_writer.writerow(row)
