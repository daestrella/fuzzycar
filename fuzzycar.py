from mf import trapmf, trimf, zbimf, sbimf, constmf
from graph import Graph
from fuzzyops import Fuzzy, Rule
import arguments

# for parameter parsing
args = arguments.parse()

# temperature (°F)
freezing = zbimf(30, 50)
cool = trimf(30, 50, 70)
warm = trimf(50, 70, 90)
hot = sbimf(70, 90)

# cloud cover (%)
sunny = zbimf(20, 40)
partly = trimf(20, 50, 80)
overcast = sbimf(60, 80)

# car speed (mph)
slow = zbimf(25, 75)
fast = sbimf(25, 75)

DOMAIN = (0, 100)
WINDOW = (12, 6)

# inferencing using Mamdani system
inferred_speed = Fuzzy.aggregate([
    Rule((sunny(args.cloud), min, warm(args.temp)), fast), # sunny AND warm --> slow
    Rule((partly(args.cloud), min, cool(args.temp)), slow) # partly cloudy AND cool --> fast
    ])

# graphing
graph = Graph(title=f'Inferred car speed based on temperature (T = {args.temp}°F) '
                    f'and cloud coverage (c = {args.cloud}%)',
              domain=DOMAIN, winsize=WINDOW, xlabel='speed (mph)', ylabel='membership degree')

graph.plot_mf(function=fast, color='orange', legend='fast function', shaded=False)
graph.plot_mf(function=slow, color='green', legend='slow function', shaded=False)
graph.plot_mf(function=inferred_speed, color='blue', legend='Aggregated fast and slow functions', shaded=True)

graph.plot_line(Fuzzy.defuzzify(inferred_speed, startpos=DOMAIN[0], endpos=DOMAIN[1]), 'Inferred car speed')
