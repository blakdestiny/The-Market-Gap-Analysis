The Sugar Trap - Market Gap Analysis

Open Food Facts · Helix CPG Partners · a "Blue Ocean" study for healthy snacking

 A. Executive Summary

Analysis of the Open Food Facts snack category dataset reveals a clear market gap: Chocolate/Candy and Cookies/Biscuits are the two largest snack categories by volume, yet fewer than 8% of products in either fall into the "High Protein + Low Sugar" quadrant. The gap is validated independently by Nutri-Score data, where this quadrant scores an A rating at roughly 4x the rate of any other quadrant. We recommend a Chocolate/Candy product targeting "10g protein and under 8g sugar per 100g"; a profile already achieved by ~7,300 existing "winner" products in the dataset, most commonly built on soy, oat, or milk protein rather than whey isolate. This represents a high-volume, low-competition opportunity aligned with both consumer demand and independent nutrition scoring.

 B. Project Links

 Link to Notebook: https://colab.research.google.com/drive/1lvmSm5BbHwV5Z36xWZqMgTFuQQ_7nm0U#scrollTo=vWVP7lN4LlId
 Link to Dashboard: https://colab.research.google.com/drive/1lvmSm5BbHwV5Z36xWZqMgTFuQQ_7nm0U#scrollTo=vWVP7lN4LlId&fullscreenOutput=true [https://colab.research.google.com/drive/1lvmSm5BbHwV5Z36xWZqMgTFuQQ_7nm0U#scrollTo=o9wnoVgceOZB&fullscreenOutput=true]
 Link to Presentation:
 C. Technical Explanation

 Data Cleaning
The raw Open Food Facts export (~12.6GB uncompressed) was streamed in 100,000-row chunks directly from the gzipped source, filtering each chunk to snack-relevant categories (`snack`, `biscuit`, `cookie`, `chip`, `cracker`, `bar`, `chocolate`, `cereal`, `candy`) before ever holding the full dataset in memory. From there:

- Rows missing `product_name`, `sugars_100g`, or `proteins_100g` were dropped rather than imputed, since guessing macro values would bias the clustering the whole analysis depends on.
- Nutrient columns were coerced to numeric with `pd.to_numeric(errors="coerce")`, since a handful of non-numeric entries in the source data were silently forcing entire columns to `object` dtype.
- Per-100g values were bounded to a biologically plausible 0–100g range; anything outside that is a data-entry error, not a real product.
- `fat_100g` nulls were filled with 0 rather than dropped, since fat isn't one of the two core analysis axes (sugar/protein) and dropping on it would cost rows for no analytical benefit.
- Exact duplicate products (same name + same macros) were removed.

 Category Wrangler
`categories_tags` was keyword-matched (in priority order, most-specific first) into 7 high-level buckets; Bars, Chips/Crisps, Crackers, Cookies/Biscuits, Chocolate/Candy, Nuts/Seeds, Cereal/Granola — plus an "Other" catch-all for anything unmatched.

 Nutrient Matrix & Gap Identification
Products were split into four quadrants using the dataset-wide median sugar and protein values as cutoffs (not a fixed nutrition-science standard — this threshold choice is called out here for transparency). Cross-tabulating category against quadrant showed Chocolate/Candy and Cookies/Biscuits; the two highest-volume categories; with the lowest share of products in the "High Protein + Low Sugar" quadrant (7.7% and 5.5% respectively), while smaller categories like Cereal/Granola and Nuts/Seeds were already saturated with healthy options (~68–70% share). High volume + low healthy-share is the definition of the gap used here.

 Candidate's Choice: Nutri-Score Cross-Validation
Since sugar and protein alone don't capture everything a consumer or regulator considers "healthy," the identified gap quadrant was cross-referenced against Nutri-Score; an independent, industry-standard rating already present in the source data but unused elsewhere in this analysis. This was added because it answers the obvious follow-up question a client would ask: "healthy by whose definition?" The result validated the approach: products in the High Protein + Low Sugar quadrant earned an A rating 23.5% of the time; roughly 4x the rate of any other quadrant; and an E rating only 9.6% of the time, versus 55–71% in the sugar-heavy quadrants. Notably, ~32% of products in this quadrant still scored D or E, indicating protein and sugar targets alone won't guarantee a top Nutri-Score; other factors like saturated fat and additives will need attention during formulation.

 Bonus: Hidden Gem Ingredient Analysis
Ingredient text for all high-protein products was keyword-matched against common protein sources. The three most common were "Soy (12.9% of products)", "Oats (6.6%)", and "Milk Protein (3.2%)"; suggesting a plant-forward or dairy-adjacent formulation, rather than pure whey isolate, is both common and commercially viable in this space, offering a realistic ingredient path for the recommended Chocolate/Candy product.
