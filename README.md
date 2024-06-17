

---

# DWAHS Web Portal

## Overview

The DWAHS (Drinking Water Access and Hygiene Survey) web portal is designed to collect data on household water access, treatment practices, hygiene habits, and health history. This data will be used to investigate the correlation between clean water access and cholera vulnerabilities in different regions.

## Features

- **Multi-step Data Collection**: The survey is divided into multiple sections to streamline data entry.
- **Interactive Navigation**: Users can navigate through the survey sections using "Next" and "Previous" buttons.
- **Data Validation**: Input fields are designed to capture data accurately, ensuring high data quality.

## Data Schema

### Household Information
| Field Name              | Data Type  | Description                                              |
|-------------------------|------------|----------------------------------------------------------|
| district                | VARCHAR(50)| District of the household                                 |
| rural_urban             | VARCHAR(10)| Rural or urban residence of the household                 |
| num_household_members   | INTEGER    | Number of people living in the household                  |
| residential_area        | VARCHAR(50)| Specific residential area within Harare                   |
| house_number            | VARCHAR(50)| House or plot number                                      |
| street                  | VARCHAR(50)| Street or road name                                       |
| city                    | VARCHAR(50)| City (Harare in this case)                                |
| country                 | VARCHAR(50)| Country (Zimbabwe in this case)                           |

### Water Source Access
| Field Name              | Data Type  | Description                                              |
|-------------------------|------------|----------------------------------------------------------|
| water_source_type       | VARCHAR(50)| Type of water source used (tap, borehole, protected well, other) |
| water_source_description| VARCHAR(255)| Detailed description of the water source                 |
| water_source_quality    | VARCHAR(50)| Perceived water quality (Clean/Contaminated)              |
| tap_water_access        | BOOLEAN    | Does the household have access to tap water? (True/False) |
| frequency_of_access     | INTEGER    | Frequency of tap water access (number of days per week)   |

### Water Treatment Practices
| Field Name              | Data Type  | Description                                              |
|-------------------------|------------|----------------------------------------------------------|
| water_treatment_methods | VARCHAR(255)| Methods used for water treatment (boiling, chlorine treatment, other) |
| treatment_consistency   | VARCHAR(50)| Consistency of water treatment practices (Always/Sometimes/Never) |

### Hygiene Practices
| Field Name              | Data Type  | Description                                              |
|-------------------------|------------|----------------------------------------------------------|
| handwashing_frequency   | VARCHAR(50)| Frequency of handwashing among household members (times per day) |
| sanitation_facilities   | VARCHAR(50)| Availability and condition of sanitation facilities (toilets, handwashing stations) |
| wastewater_disposal     | VARCHAR(50)| Method of wastewater disposal                            |
| solid_waste_disposal    | VARCHAR(50)| Method of solid waste disposal                           |

### Health History
| Field Name              | Data Type  | Description                                              |
|-------------------------|------------|----------------------------------------------------------|
| cholera_history         | BOOLEAN    | History of cholera or other waterborne diseases in the household (True/False) |
| recent_waterborne_illness| BOOLEAN   | Recent health issues related to water quality (diarrhea, gastroenteritis, etc.) (True/False) |

### Additional Information
| Field Name              | Data Type  | Description                                              |
|-------------------------|------------|----------------------------------------------------------|
| water_access_challenges | VARCHAR(255)| Factors affecting access to clean water (seasonal variations, water rationing, etc.) |


## License

This project is licensed under the MIT License. See the LICENSE file for more information.

## Acknowledgements

This project is developed by Quantacrusaders for the DWAHS (Drinking Water Access and Hygiene Survey) initiative. Special thanks to all contributors and the community for their support.

---
