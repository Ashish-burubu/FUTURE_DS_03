# Marketing Funnel & Conversion Performance Analysis 📊

## 📌 Project Overview
This repository contains the analysis for **Task 3: Marketing Funnel & Conversion Performance Analysis** as part of the **Future Interns Data Science & Analytics Internship (2026)**.

The objective of this project is to analyze customer conversion funnels, evaluate channel effectiveness, identify drop-off bottlenecks, and provide data-driven recommendations to optimize campaign ROI and conversion rates.

---

## 📅 Dataset
- **Name:** Bank Marketing Campaign Dataset (UCI Machine Learning Repository)
- **Records:** 45,211 contacts across multi-stage promotional campaigns.

---

## 🔑 Key Analytics & Insights

1. **Overall Funnel Breakdown:**
   - **Top Funnel (Total Contacts):** 45,211 users (100%)
   - **Mid Funnel (Engaged Leads > 3 min call duration):** 20,042 users (44.33%) — **55.67% initial drop-off**
   - **Bottom Funnel (Converted Customers):** 5,289 users (11.70%) — **73.61% mid-to-bottom drop-off**

2. **Channel Performance:**
   - **Cellular:** Highest conversion rate (**14.92%**) with 4,369 conversions.
   - **Telephone:** 13.42% conversion rate.
   - **Unknown / Untracked:** Lowest conversion rate (**4.07%**).

3. **Contact Frequency Fatigue:**
   - Conversion peaks at **1 contact attempt (14.60%)** and diminishes as attempts increase. Attempts beyond 4 contacts result in severe sub-5% conversion yields.

4. **Retargeting Power:**
   - Leads with a **successful outcome from previous campaigns converted at 64.73%**, compared to 9.16% for cold prospects.

---

## 🚀 Strategic Recommendations
- **Optimize Channel Mix:** Focus sales outreach budget on cellular contacts and eliminate untracked contact methods.
- **Implement Frequency Capping:** Limit contact attempts to 3 contacts per campaign cycle to prevent lead fatigue.
- **Prioritize Prior-Success Segments:** Build dedicated retargeting workflows for past campaign buyers to capitalize on the 64.73% conversion benchmark.

---

## 🛠️ How to Run
```bash
# Clone the repository
git clone [https://github.com/your-username/marketing-funnel-analysis.git](https://github.com/your-username/marketing-funnel-analysis.git)

# Navigate to project directory
cd marketing-funnel-analysis

# Install requirements
pip install pandas numpy matplotlib seaborn

# Run analysis script
python funnel_analysis.py
