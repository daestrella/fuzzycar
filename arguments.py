import argparse

def parse():
    parser = argparse.ArgumentParser(
            prog='fuzzycar',
            description=f'Outputs the car speed given the temperature and '
                        f'cloud coverage percentage.')

    parser.add_argument('temp', type=float, help='temperature in degrees Fahrenheit')
    parser.add_argument('cloud', type=float, help='cloud coverage in percentage')

    return parser.parse_args()
