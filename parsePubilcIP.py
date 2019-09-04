import requests
import argparse

parser = argparse.ArgumentParser(description='Generate a single-column list of public location IP addresses')
parser.add_argument('-o', '--outputfile', help='File name to write IP addresses to (default=output.txt)',
                    default='output.txt')
parser.add_argument('-e', '--endpoint', help='Endpoint of the Public Location IP addresses in JSON format', default='https://s3.amazonaws.com/nr-synthetics-assets/nat-ip-dnsname/production/ip.json')
args = parser.parse_args()

output_file = args.outputfile
endpoint = args.endpoint

response = requests.get(endpoint)

if response.status_code == requests.codes.ok:
    print('Success: Public location IP addresses returned')
    output = ''

    publicLocations_json = response.json()
    addressCount = 0

    for location in publicLocations_json:
        # parse JSON for IP addresses
        for address in publicLocations_json[location]:
            output = output + address + '\n'
            addressCount += 1

print(str(addressCount) + ' IP addresses parsed.')

file = open(output_file, 'w')
file.write(output)
file.close()

print('IP addresses written to ' + output_file)
print('Script complete')


