from flask import Flask, render_template, url_for

app = Flask(__name__)
@app.route('/design')
def design():
    return render_template('design.html')

@app.route('/datahandle')
def datahandle():
    return render_template('datahandle.html')

@app.route('/analysis')
def analysis():
    analyses = [
        {
            "title": "Top Categories by Revenue",
            "description": "Ranking by revenue of the various product categories has been represented graphically using a bar graph whereby Apparel emerged as the most lucrative segment earning more than $4 million followed by Nest-USA. While these two categories act as super-categories that garner the greatest sales, others such as Office, Drinkware and Lifestyle categories attract medium sales. The Notebooks & Journals and Headgear categories generate comparatively small revenues are at the lower end of the company’s performance spectrum. This increases Apparel’s market share and points towards the idea of value creation strategy pertaining to the top categories and considering how to increase the sales of the weak categories.",
            "image_url": "image1.png"
        },
        {
            "title": "Top Products by Revenue",
            "description": "This can be seen from the bar graph on the highest revenue generating products , where the Nest® Cam Outdoor Security Camera – USA received revenue of more than $800,000, Nest® Learning Thermostat 3rd Gen – Stainless Steel and, Nest® Cam Indoor Security Camera – USA indicating a growing market in home security and automation. The Google Sunglasses and Nest® Protect Smoke + CO Alarms contribute moderately and products with lower revenues like Google 22 oz Water Bottle, Nest® Cam IQ – USA also make the list. This means that some categories should be targeted based on the fact that they are smart home products while the middle performers present more chance to expand by implementing certain tactics.",
            "image_url": "image2.png"
        },
        {
            "title": "Sales Trends Over Time",
            "description": "The line graph represents **monthly sales revenue for the year 2017** depicting the amount of sales in each month. For **April**, there is a sharp increase in revenues to just over $2 million, this may probably be as a result of promotions or seasonal factors. By reef or fall, then, revenue falls in **May** before rising again in **July**, and tapering off towards the end of the year, or **October**. Lastly, **November and December** presumably due to holiday seasons may record a slightly higher sales than the end of the month figure. These trends show the potential of increasing loads during the crowd months such as April and July while managing the low months using special measures.",
            "image_url": "image3.png"
        },
        {
            "title": "Tax and Delivery Cost Impact",
            "description": "The omnibus horizontal bar chart above shows the amount of dollars which defines the product categories chosen as profitable. When it comes to profit, “Apparel” is ranked the highest having a much higher profit than the other categories, “Nest-USA,” “Office“, has the next highest profits. I find products with moderate profitability in some categories like “Drinkware,” “Lifestyle,” and “Nest,” whereas others like “Waze,” “Accessories,” and “Android” bring little to the bottom line. What is more, it underlines concentration of many companies within several broadband categories thus implying that these categories may be a key concern for the firms with regard to their income generation and business strategy.",
            "image_url": "image4.png"
        },
        {
            "title": "Profitability Analysis",
            "description": "The bar chart shows the average of tax and delivery cost effects (%) by different product types. Two distinct bars represent each category: The first is concerned with the positive tax implication on the organization (blue), the second is about the positive delivery impact on the organization (green). Delivery costs were mostly higher across categories from which we can see spikes in subcategories such as “Bottles,” “Nest-Canada,” and “Waze.” On the other hand, an impact on tax has been moderate and stable over different categories with slight fluctuations. Relative to delivery costs taxes make a minor contribution to the relative costs and fluctuates effectively with respect to the types of products delivered indicating perhaps the weights that delivery costs have in pricing strategies of the products.",
            "image_url": "image5.png"
        },
        {
            "title": "High-Tax Impact Products",
            "description": "The horizontal bar chart then categorizes the revenue by products according to the percentage of tax impact. The Compact Journal with Recycled Pages has the highest tax impact and is set significantly apart from the rest of the products. In order immediately following several Nest® products including the “Thermostat E,” “Cam IQ,” and “Learning Thermostat 3rd Gen,” which ranked do account for relatively high tax percent. Also, two products – Google Tee Red and the YouTube Kids Tee Black are the product least technologically with their tax impacts slightly over 10% and forming part of the top ten products. This chart shows the best way that particular products for example those manufactured under the Nest® brand in particular are subjected to a higher tax levels.",
            "image_url": "image6.png"
        },
        {
            "title": "Revenue by Day of the Week",
            "description": "The second graphic type is the horizontal bar chart, which shows day by day revenue and suggests weekly fluctuations in business activity. Studied days show that Wednesday yields the highest revenues of approximately $3,500,000 while Tuesday yields about $3 million. Friday and Monday exhibit almost the same sales; both days totaling $2.5 million worth of sales created. Thursday undergoes the same level of overall revenue as does Monday and Friday. : Revenue is extremely low during the weekends; Saturday and Sunday recorded slightly over $1 million, which is way less than a third of what was generated on Wednesday. To show the revenue patterns, the color coding in the graph uses blue shades for days that scored the highest performances, gray for the second best and top red tones for the worst performers, thus making comparisons easy.",
            "image_url": "image7.png"
        },
        {
            "title": "Item Popularity",
            "description": "This graph shows the most commonly bought items in online sales. Used in conjuction with revenue graphs, we can tell which products are most important to our business and customers.",
            "image_url": "image8.png"
        }
    ]
    return render_template('analysis.html',analyses=analyses)

@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/')
def base():
    return render_template('nav.html')
# @app.route('/')
# def home():
#     # Sample data to display

    
#     return render_template('index-1.html', analyses=analyses)

if __name__ == '__main__':
    app.run(debug=True)
