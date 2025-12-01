# 🔥 Jules Streak Finder

> A Python tool for finding and analyzing streaks in sequential data

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Data Analysis](https://img.shields.io/badge/Data-Analysis-orange?style=flat)](https://github.com/zetroretron/jules-streak-finder)

---

## 📋 Overview

**Jules Streak Finder** is a Python utility designed to identify and analyze streaks in sequential data. Whether you're tracking winning streaks, consecutive events, or patterns in time-series data, this tool provides an efficient way to find and measure streaks.

---

## ✨ Features

- **Streak Detection**: Automatically find consecutive sequences in data
- **Customizable Criteria**: Define what constitutes a "streak" for your use case
- **Statistical Analysis**: Get insights about streak lengths and patterns
- **Easy Integration**: Simple API for use in your Python projects
- **Flexible Input**: Works with various data formats

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/zetroretron/jules-streak-finder.git
   cd jules-streak-finder
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 Usage

### Basic Example

```python
from jules_streak_finder import find_streaks

# Sample data
data = [1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1]

# Find streaks of 1s
streaks = find_streaks(data, value=1)

print(f"Found {len(streaks)} streaks")
for i, streak in enumerate(streaks, 1):
    print(f"Streak {i}: Length {streak['length']}, Position {streak['start']}-{streak['end']}")
```

### Advanced Usage

```python
from jules_streak_finder import StreakAnalyzer

# Create analyzer
analyzer = StreakAnalyzer(data)

# Find all streaks
all_streaks = analyzer.find_all_streaks()

# Get statistics
stats = analyzer.get_statistics()
print(f"Longest streak: {stats['max_length']}")
print(f"Average streak length: {stats['avg_length']}")
print(f"Total streaks: {stats['count']}")
```

---

## 📊 Use Cases

### Sports Analytics
Track winning/losing streaks in sports data:
```python
game_results = ['W', 'W', 'W', 'L', 'W', 'W', 'L', 'W', 'W', 'W']
winning_streaks = find_streaks(game_results, value='W')
```

### Time Series Analysis
Find consecutive periods of specific conditions:
```python
temperature_above_30 = [True, True, False, True, True, True, False]
heatwave_periods = find_streaks(temperature_above_30, value=True)
```

### User Engagement
Analyze consecutive days of user activity:
```python
daily_logins = [1, 1, 1, 0, 0, 1, 1, 1, 1, 0]
engagement_streaks = find_streaks(daily_logins, value=1)
```

---

## 📁 Project Structure

```
jules-streak-finder/
├── README.md              # This file
├── requirements.txt       # Python dependencies
├── jules_streak_finder/   # Main package (if structured)
│   ├── __init__.py
│   ├── finder.py         # Core streak finding logic
│   └── analyzer.py       # Statistical analysis
└── examples/             # Usage examples
    └── basic_usage.py
```

---

## 🔧 API Reference

### `find_streaks(data, value, min_length=1)`

Find all streaks of a specific value in the data.

**Parameters:**
- `data` (list): The sequential data to analyze
- `value` (any): The value to find streaks of
- `min_length` (int): Minimum streak length to include (default: 1)

**Returns:**
- `list`: List of streak dictionaries with `start`, `end`, and `length`

### `StreakAnalyzer(data)`

Class for advanced streak analysis.

**Methods:**
- `find_all_streaks()`: Find all streaks in the data
- `get_statistics()`: Get statistical summary of streaks
- `get_longest_streak()`: Get the longest streak
- `filter_by_length(min_length, max_length)`: Filter streaks by length

---

## 📚 Examples

### Example 1: Finding Consecutive Days

```python
# Track daily exercise (1 = exercised, 0 = didn't)
exercise_log = [1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1]

streaks = find_streaks(exercise_log, value=1, min_length=2)

for streak in streaks:
    print(f"Exercised for {streak['length']} consecutive days "
          f"(days {streak['start']}-{streak['end']})")
```

### Example 2: Stock Price Analysis

```python
# Track days when stock price increased
price_increases = [True, True, False, True, True, True, False, True]

bull_runs = find_streaks(price_increases, value=True, min_length=2)

print(f"Found {len(bull_runs)} bull runs of 2+ days")
```

---

## 🧪 Testing

Run tests (if available):

```bash
python -m pytest tests/
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the MIT License.

---

## 👨‍💻 Author

**GitHub:** [@zetroretron](https://github.com/zetroretron)  
**Institution:** IIT Madras

---

## 🎯 Future Enhancements

- [ ] Support for multi-dimensional data
- [ ] Visualization of streaks
- [ ] Export results to CSV/JSON
- [ ] Command-line interface
- [ ] Performance optimizations for large datasets

---

## 📞 Support

For questions or issues:
- Open an issue on [GitHub Issues](https://github.com/zetroretron/jules-streak-finder/issues)
- Check existing issues for solutions

---

**Find your streaks! 🔥**
