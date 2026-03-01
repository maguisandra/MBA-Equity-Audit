# MBA Admission Equity Audit
**Analysis of MBA admissions equity and inclusion using synthetic data – evaluates gender and racial disparities with insights from Human Capital Theory, Social Reproduction, and SDG 4.**

---

## 📘 README

### Equity and Inclusion Analysis Using Synthetic Data

This project examines MBA admission outcomes through the lens of **equity and inclusion**, analyzing whether applicants are treated fairly across **gender** and **race**, and exploring possible **social reproduction** patterns within institutional selection.

⚠️ **Important**: Dataset is **synthetic** and does not represent real applicants.

---

## 1️⃣ Project Context and Theoretical Framework

### Objective
- Evaluate fairness in MBA admissions by gender and race  
- Identify potential structural barriers or biases in selection

### Theoretical Framework
- **Human Capital Theory (Becker, 1964)**: Skills, knowledge, and qualifications (GPA, GMAT) increase productivity and admission chances  
- **Social Reproduction Theory (Bourdieu, 1970)**: Institutions can **reproduce social inequalities**, favoring candidates whose background matches system expectations  
- **SDG 4 – Quality Education**: Ensures equitable access to quality education. Disparities in admission conflict with this goal

---

## 2️⃣ Data Source and License

- **Origin**: Synthetic data inspired by aggregated statistics from Wharton Class of 2025  
- **Platform**: [Kaggle - MBA Admission Dataset](https://www.kaggle.com)  
- **License**: [Apache 2.0](https://www.apache.org)  
- **Usability Score**: 10/10  


> Contains **no real individual information**; purely illustrative

---

## 3️⃣ Data Preparation and Cleaning

1. Imported dataset into Python  
2. Cleaning and preprocessing:  
   - `race = null` → replaced with `International`  
   - `admission = null` → interpreted as `Deny`  
3. Imported into Power BI via Python script  
4. Final validation and transformations in Power Query before report building

---

## 4️⃣ Dataset Structure

| Column | Description |
|--------|-------------|
| `application_id` | Unique identifier |
| `gender` | Male / Female |
| `international` | TRUE / FALSE |
| `gpa` | GPA on 4.0 scale |
| `major` | Business / STEM / Humanities |
| `race` | White / Black / Asian / Hispanic / Other / International |
| `gmat` | GMAT score (out of 800) |
| `work_exp` | Years of work experience |
| `work_industry` | Consulting, Finance, Technology, etc. |
| `admission` | Admit / Waitlist / Deny |

---

## 5️⃣ Power BI Report Structure

### Page 1 – Applicant Landscape
- Gender and race distribution  
- Major and industry distribution  
- Academic background (GPA, GMAT)  
- **Key finding**: 63.66% of applicants were male at entry

### Page 2 – Institutional Selection Logic
- Distribution of GMAT, GPA, and work experience  
- Analysis of selection thresholds  
- Checks whether selection is **merit-based**

### Page 3 – Equity Audit: Admission Outcomes & Social Reproduction

#### Gender Outcomes
- Admission: 50% Male / 50% Female  
- Despite male overrepresentation at entry (63.66%), outcomes achieve parity ✅

#### Racial Outcomes

| Race | Entry % | Admitted % | Δ | GMAT avg (Admitted) |
|------|---------|------------|---|-------------------|
| International | 29.74% | 30.89% | ↑ +1.15 | 689.89 |
| White | 23.51% | 27.11% | ↑ +3.60 | 692.42 |
| Asian | 18.52% | 21.11% | ↑ +2.59 | 694.11 |
| Black | 14.79% | 8.89% | ↓ -5.90 | 699.00 |
| Hispanic | 9.62% | 6.89% | ↓ -2.73 | 699.52 |
| Other | 3.83% | 5.11% | ↑ +1.28 | 685.87 |

**Analysis**:  
- Black & Hispanic applicants have the **highest GMAT averages**, yet their representation **declines at admission**  
- White, Asian, International, and Other increase or remain stable  
- High entry performance does **not guarantee equity at exit** → **social reproduction effect**

---

## 6️⃣ Key Metrics: Average GMAT (Admitted)

| Race | GMAT avg (Admitted) | Δ vs Overall Avg (692.73) |
|------|-------------------|---------------------------|
| Hispanic | 699.52 | +6.79 |
| Black | 699.00 | +6.27 |
| Asian | 694.11 | +1.38 |
| White | 692.42 | -0.31 |
| International | 689.89 | -2.84 |
| Other | 685.87 | -6.86 |

**Insight**:  
- Hispanic and Black applicants must exceed the overall average to be admitted  
- International and Other admitted below average  
- Suggests **structural barriers** for certain groups

---

## 7️⃣ Entry vs Exit Percentages

| Race | Entry % | Admitted % | Change | Trend |
|------|---------|------------|--------|-------|
| International | 29.74% | 30.89% | ↑ +1.15 | ✅ |
| White | 23.51% | 27.11% | ↑ +3.60 | ✅ |
| Asian | 18.52% | 21.11% | ↑ +2.59 | ✅ |
| Black | 14.79% | 8.89% | ↓ -5.90 | ❌ |
| Hispanic | 9.62% | 6.89% | ↓ -2.73 | ❌ |
| Other | 3.83% | 5.11% | ↑ +1.28 | ✅ |

**Interpretation**:  
- Black and Hispanic representation **declines sharply** despite **highest GMAT averages**  
- Shows some groups face **higher thresholds** to compete

---

## 8️⃣ Limitations

- Dataset is **synthetic**  
- Results **do not reflect real institutions**  
- Findings are **illustrative and educational only**

---

## 9️⃣ Conclusion

- **Gender**: Outcomes achieve parity, correcting male overrepresentation  
- **Race**: Disparities persist despite similar academic profiles  
- Selection is **not perfectly neutral**; structural barriers exist  
- Highlights the need for **multi-dimensional evaluation** of admissions processes

> Even with high merit indicators, some groups face disadvantages → relevance of **Human Capital Theory**, **Social Reproduction Theory**, and **SDG 4**

---

## ✅ Executive Insights

1. Entry-level distribution: relatively balanced  
2. Exit-level outcomes: some groups increase, others decrease  
3. High academic performers (GMAT) are not necessarily the most represented at admission  
> Reveals **partial inequity** and **social reproduction** in MBA admissions

