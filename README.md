# UIC Argonne Project --- High Performance Computing --- MS Research Project( 6 - Month - Project)

The project focuses on the THETA HPC System (https://www.alcf.anl.gov/alcf-resources/theta), which served the Argonne National Lab for 10 years. I have my gratitude for this System. The study defines correlating HPC job logs with hardware-error events on Argonne's Theta supercomputer to enable predictive maintenance and improve system reliability.

## Project Goals
1. The primary goal of this project was to enhance the reliability of High-Performance Computing (HPC) systems by developing a methodology to correlate job logs with hardware-error events.
2. This approach aims to uncover patterns linking low-level component faults to high-level job failures, enabling the development of predictive-maintenance strategies.

## Network Topology And Data
1. The Theta system has a hierarchical architecture (cabinets, chassis, blades, nodes) and a DragonFly topology.
2. The study utilized data from the Theta supercomputer at Argonne National Laboratory.
3. The dataset included over 91,000 job records and 136,000 hardware-error events from 2019.

## Methodology 
1. Direct Correlation
2. Time-Based Correlation
3. Spatial Correlation
4. Efficient Time-Based Correlation with Interval Trees - Interval Trees were implemented to optimize the time-based correlation process, reducing the time complexity of finding overlapping job intervals from O(N) to O(log N) for each hardware error event (where N is the number of job intervals). This optimization significantly improves the efficiency of the analysis, especially for large datasets.

## Potential Impact
1. The correlations identified in this study can be used to develop predictive-maintenance strategies.
2. Proactive repairs can be scheduled based on predicted failures, minimizing resource waste and improving job throughput.
3. The insights can inform the design of more resilient HPC infrastructures and improve workload allocation.

## Conclusion

This research reflects my ability to tackle complex challenges in large-scale distributed systems, applying data analysis and algorithmic optimization to improve system reliability. 
The project showcases my skills in:
1. HPC Systems: Understanding HPC architectures and the DragonFly network topology.
2. Data Analysis: Proficiency in processing and correlating large datasets (91,000+ job logs, 136,000+ hardware errors).
3. Algorithm Design: Implementation of efficient algorithms, including Interval Trees for O(log N) time complexity.
4. Problem-Solving: Developing a methodology to address a critical issue in HPC, minimizing downtime through predictive maintenance.


##  Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/man0j-012/UIC_Argonne_Theta_Project.git
   cd UIC_Argonne_Theta_Project
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the analysis**
   - **Using full data** (requires raw CSVs in `data/raw/`):
     ```bash
     python scripts/run_analysis.py --year 2019
     ```
   - **Using sample data** (for quick demos):
     ```bash
     python scripts/run_analysis.py --year 2019 --sample
     ```

## 📁 Repository Structure

```
UIC_Argonne_Theta_Project/
├─ docs/                 # Final report and diagrams
│  ├ MS_Project_CS_597_Report.pdf
│  ├ dataset_relationship_diagram
│  └ methodology_workflow_diagram
├─ src/                  # Core modules (mapping, correlation, plotting)
├─ scripts/              # CLI entrypoints to preprocess, correlate, and analyze
├─ data/                 # Data storage
│  ├ raw/                # Large CSVs & logs (gitignored)
│  └ sample/             # Small sample files for quick testing
├─ figures/              # Generated plots (gitignored)
├─ tests/                # pytest suites for core functionality
├─ .gitignore            # Ignored files/folders
├─ requirements.txt      # Python dependencies
├─ LICENSE               # MIT License
└─ README.md             # This file
```

## 📊 Sample Output

![Sample Correlation Heatmap](figures/failure_to_error_ratio_heatmap.png)

*See `figures/` for all generated plots.*

## 📄 Documentation

- **Full project report:** [docs/MS_Project_CS_597_Report.pdf](docs/MS_Project_CS_597_Report.pdf)

## 🧪 Testing

Run unit tests with:
```bash
pytest --maxfail=1 --disable-warnings -q
```

## Gratitude Message:- 
Huge Thanks to my Professor Zhiling Lan, Scientists from Argonne National Lab - Dr.Kevin Brown, Dr.Tanwi Mallick

## 📄 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

