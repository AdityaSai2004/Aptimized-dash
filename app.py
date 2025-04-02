import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from streamlit_extras.colored_header import colored_header
from streamlit_extras.metric_cards import style_metric_cards
import streamlit_nested_layout
import time

# Sample Data (replace with actual data from your table)
data = {
    "AI Solution": [
        "IoT", "Blockchain powered AI systems", "Hyperpersonalisation", "Recommendation engine", "Chatbot",
        "Social media manager", "AI adverts", "Ticket handling", "Review summariser", "Smart data cleaning",
        "AI powered SEO engine", "AI agent copy writer", "Analytics dashboard", "Custom AI/ML solutions",
        "Business analytics and optimisation"
    ],
    "Ecommerce": ["✔", "", "✔", "✔", "✔", "✔", "✔", "", "✔", "", "✔", "", "", "", "✔"],
    "Gcloud": ["", "✔", "", "✔", "✔", "", "", "", "", "", "", "", "", "✔", ""],
    "HR Tech Solutions": ["", "", "", "", "", "", "", "", "", "", "", "", "", "✔", ""],
    "Managed IT Services": ["", "", "", "", "", "", "", "", "", "", "", "", "", "✔", ""],
    "Modern Tech Support": ["✔", "", "", "", "", "", "", "✔", "", "", "", "", "", "✔", ""],
    "Govt Solutions": ["", "", "", "", "", "", "", "✔", "", "", "", "", "", "✔", ""],
    "Telecommunications": ["", "", "", "", "", "", "", "✔", "", "", "", "", "", "✔", ""],
    "Data Productization": ["", "", "", "", "", "", "", "", "", "", "", "", "✔", "", ""],
    "SAP": ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    "Salesforce": ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    "Adobe": ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    "Blockchain": ["", "✔", "", "", "", "", "", "", "", "", "", "", "", "✔", "✔"]
}

df = pd.DataFrame(data)

def set_light_theme(fig):
    fig.update_layout(
        template="plotly_white",
        paper_bgcolor="white",
        plot_bgcolor="white",
        font=dict(color="black"),  # Set all text to black
        margin=dict(l=40, r=40, t=50, b=40),
        xaxis=dict(
            showgrid=True,  
            gridcolor="lightgray",  # Light gray grid for visibility
            tickfont=dict(color="black"),  # X-axis labels in black
            title=dict(text="X-Axis Title", font=dict(color="black"))  # X-axis title in black
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor="lightgray",
            tickfont=dict(color="black"),  # Y-axis labels in black
            title=dict(text="Y-Axis Title", font=dict(color="black"))  # Y-axis title in black
        ),
    )
    return fig

# Function to convert '✔' to 1 and '' to 0
def transform_data_for_analysis(dataframe):
    df_copy = dataframe.copy()
    for col in df_copy.columns:
        if col != 'AI Solution':
            df_copy[col] = df_copy[col].apply(lambda x: 1 if x == '✔' else 0)
    return df_copy

# Custom CSS
def apply_custom_css():
    st.markdown("""
<style>
    /* Ensure dropdown background is white and text is black */
    div[data-baseweb="select"], 
    div[data-baseweb="popover"], 
    div[data-baseweb="menu"], 
    div[role="listbox"] {
        background-color: #FFFFFF !important; /* ✅ White background */
        color: #000000 !important; /* ✅ Black text */
        border: 1px solid #E2E8F0 !important;
    }

    /* ✅ Dropdown Options */
    div[role="option"] {
        background-color: #FFFFFF !important; /* ✅ White */
        color: #000000 !important; /* ✅ Black */
    }
    div[role="option"]:hover {
        background-color: #E2E8F0 !important; /* ✅ Light Gray Hover */
        color: #000000 !important;
    }

    /* ✅ Fix selected dropdown option */
    div[data-baseweb="select"] div[role="option"][aria-selected="true"] {
        background-color: #E2E8F0 !important; /* ✅ Light Gray */
        color: #000000 !important;
    }

    /* ✅ Fix text input inside dropdown */
    div[data-baseweb="select"] input {
        background-color: #FFFFFF !important;
        color: #000000 !important;
    }

    /* ✅ Fix Scroll & Overflow */
    div[role="listbox"] {
        max-height: 300px !important;
        overflow-y: auto !important;
    }
</style>



    """, unsafe_allow_html=True)

def create_card(title, content):
    st.markdown(f"""
    <div class="card">
        <div class="card-title">{title}</div>
        {content}
    </div>
    """, unsafe_allow_html=True)

def main():
    st.set_page_config(
        page_title="AI Solutions Dashboard",
        page_icon="🚀",
        layout="wide", 
        initial_sidebar_state="expanded"
    )
    
    apply_custom_css()
    
    # Header with logo and title
    # col1, col2 = st.columns([1, 5])
    # with col1:
    #     st.image("Full_Logo_2_50.jpg", width=80)
    # with col2:
    st.title("🚀 Enterprise AI Solutions Portfolio")
    st.markdown("<p style='color: #6B7280; margin-top: -10px;'>Transforming businesses with cutting-edge AI solutions</p>", unsafe_allow_html=True)
    
    # Create a loading spinner
    with st.spinner("Loading dashboard..."):
        time.sleep(0.5)  # Simulate loading time
        
        # Analytics section
        st.markdown("---")
        colored_header(
            label="Portfolio Overview",
            description="Key statistics and insights",
            color_name="blue-70"
        )
        
        # Transformed dataframe for analysis
        df_analysis = transform_data_for_analysis(df)
        
        # Overview metrics
        # col1, col2, col3, col4 = st.columns(4)
        # with col1:
        #     st.metric(
        #         label="Total AI Solutions", 
        #         value=len(df),
        #         delta="15 Unique Technologies"
        #     )
        # with col2:
        #     st.metric(
        #         label="Industries Covered", 
        #         value=len(df.columns) - 1,
        #         delta="12 Verticals"
        #     )
        # with col3:
        #     total_implementations = df_analysis.iloc[:, 1:].sum().sum()
        #     st.metric(
        #         label="Total Implementations", 
        #         value=int(total_implementations),
        #         delta=f"{int(total_implementations/((len(df.columns)-1)*len(df))*100)}% Coverage"
        #     )
        # with col4:
        #     top_solution = df_analysis.iloc[:, 1:].sum(axis=1).idxmax()
        #     top_solution_name = df.iloc[top_solution]["AI Solution"]
        #     st.metric(
        #         label="Top Solution", 
        #         value=top_solution_name,
        #         delta="Most Versatile"
        #     )
        # style_metric_cards()
        
        # Sidebar Filters
        st.sidebar.image("Full_Logo_2_50.jpg", use_container_width=True)
        st.sidebar.title("Dashboard Controls")
        
        with st.sidebar.expander("🔍 FILTER OPTIONS", expanded=True):
            industries = list(df.columns[1:])
            selected_industries = st.multiselect("Select Industries", industries, default=industries)
            
            solution_categories = [
                "All Solutions",
                "Popular Solutions (3+ industries)",
                "Specialized Solutions (1-2 industries)"
            ]
            solution_category = st.radio("Solution Category", solution_categories)
            
            # Filter based on solution category
            if solution_category == "Popular Solutions (3+ industries)":
                popular_solutions = df_analysis[df_analysis.iloc[:, 1:].sum(axis=1) >= 3]["AI Solution"].tolist()
                filtered_solutions = df[df["AI Solution"].isin(popular_solutions)]
            elif solution_category == "Specialized Solutions (1-2 industries)":
                specialized_solutions = df_analysis[df_analysis.iloc[:, 1:].sum(axis=1) <= 2]["AI Solution"].tolist()
                filtered_solutions = df[df["AI Solution"].isin(specialized_solutions)]
            else:
                filtered_solutions = df.copy()
                
            # Apply industry filter
            filtered_df = filtered_solutions[['AI Solution'] + selected_industries]
        
        with st.sidebar.expander("📊 VISUALIZATION OPTIONS", expanded=False):
            chart_type = st.selectbox(
                "Select Chart Type",
                ["Bar Chart", "Grouped Bar", "Radar Chart"]
            )
            
            color_theme = st.selectbox(
                "Color Theme",
                ["Blues", "Viridis", "Plasma", "Reds", "Greens"]
            )
            
            show_percentages = st.checkbox("Show Percentages", value=False)
        
        with st.sidebar.expander("💡 INSIGHTS", expanded=False):
            st.markdown("""
            <div style=' padding: 15px; border-radius: 8px;'>
                <h4 style='margin-top: 0;'>Key Takeaways</h4>
                <ul>
                    <li>Ecommerce has the highest AI solution adoption rate</li>
                    <li>Custom AI/ML solutions are deployed across most industries</li>
                    <li>Blockchain technologies are gaining momentum</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
        st.sidebar.markdown("---")
        st.sidebar.markdown("© 2025 NeuronWorks | v1.2.0")
        
        # Main content area with tabs
        tab1, tab2, tab3 = st.tabs(["📊 Solutions Matrix", "🔍 Deep Dive", "📈 Industry Analysis"])
        
        with tab1:
            st.markdown("### AI Solutions by Industry")
            st.markdown("This matrix shows which AI solutions can be implemented across different industries")
                        
            # Style the dataframe
            styled_df = filtered_df.set_index("AI Solution")
            st.dataframe(
                styled_df, 
                use_container_width=True,
                height=400,
                hide_index=False,
                column_config={
                    col: st.column_config.Column(
                        col,
                        help=f"AI solutions available for {col}",
                        width="medium",
                        required=True
                    ) for col in styled_df.columns
                }
            )
            
            # Create heatmap visualization
            if len(selected_industries) > 0:
                st.markdown("### Solutions Distribution Visualization")
                
                df_heatmap = transform_data_for_analysis(filtered_df)
                
                if chart_type == "Grouped Bar":
                    # Create a grouped bar chart
                    industry_data = []
                    for industry in df_heatmap.columns[1:]:
                        available = df_heatmap[df_heatmap[industry] == 1]["AI Solution"].tolist()
                        for solution in available:
                            industry_data.append({
                                "Industry": industry,
                                "AI Solution": solution,
                                "Available": 1
                            })
                    
                    if industry_data:
                        industry_df = pd.DataFrame(industry_data)
                        fig = px.bar(
                            industry_df, 
                            x="Industry", 
                            y="Available",
                            color="AI Solution",
                            title="AI Solutions by Industry",
                            labels={"Available": "Count", "Industry": "Industry", "AI Solution": "AI Solution"},
                            color_discrete_sequence=px.colors.qualitative.Plotly
                        )
                        fig.update_layout(height=500, margin=dict(l=40, r=40, t=50, b=40), barmode='group')
                        fig = set_light_theme(fig)
                        st.plotly_chart(fig, use_container_width=True)
                    else:
                        st.info("No data available for visualization with current filters.")
                    
                elif chart_type == "Bar Chart":
                    solutions_count = df_heatmap.iloc[:, 1:].sum(axis=1)
                    solutions_count = pd.DataFrame({
                        "AI Solution": df_heatmap["AI Solution"],
                        "Number of Industries": solutions_count
                    }).sort_values("Number of Industries", ascending=False)
                    
                    fig = px.bar(
                        solutions_count,
                        x="AI Solution",
                        y="Number of Industries",
                        color="Number of Industries",
                        color_continuous_scale=color_theme,
                        title="AI Solutions by Industry Coverage"
                    )
                    fig.update_layout(height=500, margin=dict(l=40, r=40, t=50, b=40))
                    fig = set_light_theme(fig)
                    st.plotly_chart(fig, use_container_width=True)
                    
                elif chart_type == "Radar Chart":
                    industry_counts = df_heatmap.iloc[:, 1:].sum(axis=0)
                    industry_counts = pd.DataFrame({
                        "Industry": industry_counts.index,
                        "Solution Count": industry_counts.values
                    })
                    
                    fig = px.line_polar(
                        industry_counts, 
                        r="Solution Count", 
                        theta="Industry", 
                        line_close=True,
                        color_discrete_sequence=px.colors.sequential.__getattribute__(color_theme)(8),
                        title="Industry AI Solution Coverage"
                    )
                    fig.update_layout(height=500, margin=dict(l=40, r=40, t=50, b=40))
                    fig = set_light_theme(fig)
                    st.plotly_chart(fig, use_container_width=True)
                
        with tab2:
            # Solution deep-dive section with better UX and visuals
            st.markdown("### AI Solution Spotlight")
            st.markdown("Explore individual AI solutions and their industry applications")
            
            col1, col2 = st.columns([1, 2])
            
            with col1:
                selected_solution = st.selectbox(
                    "Select AI Solution", 
                    filtered_df["AI Solution"].unique(),
                    key="solution_select"
                )
                
                solution_row = filtered_df[filtered_df["AI Solution"] == selected_solution]
                solution_industries = [ind for ind in selected_industries if solution_row[ind].values[0] == '✔']
                
                st.markdown(f"### {selected_solution}")
                st.markdown(f"**Industries covered:** {len(solution_industries)}/{len(selected_industries)}")
                
                # Coverage percentage
                coverage = len(solution_industries) / len(selected_industries) * 100
                st.progress(coverage/100)
                st.caption(f"{coverage:.1f}% industry coverage")
                
                # Add some descriptive text based on the solution
                solution_descriptions = {
                    "Chatbot": "AI-powered conversation agents that handle customer inquiries and support",
                    "IoT": "Internet of Things solutions with AI-powered analytics and decision making",
                    "Blockchain powered AI systems": "Secure, decentralized AI systems built on blockchain technology",
                    "Hyperpersonalisation": "Tailored customer experiences based on AI-driven insights",
                    "Recommendation engine": "Intelligent systems that suggest products or content based on user behavior",
                    "Social media manager": "AI tools for content scheduling, analysis, and engagement optimization",
                    "AI adverts": "Automated advertisement creation and optimization for better conversion",
                    "Ticket handling": "Automated support ticket routing, prioritization, and resolution",
                    "Review summariser": "AI that extracts insights from customer reviews and feedback",
                    "Smart data cleaning": "Automated data preparation and cleansing for analytics",
                    "AI powered SEO engine": "Search optimization tools using natural language processing",
                    "AI agent copy writer": "Content creation tools for marketing and communications",
                    "Analytics dashboard": "Customizable data visualization and business intelligence",
                    "Custom AI/ML solutions": "Bespoke machine learning applications for specific business needs",
                    "Business analytics and optimisation": "End-to-end business performance analysis and enhancement"
                }
                
                if selected_solution in solution_descriptions:
                    st.info(solution_descriptions[selected_solution])
                
            with col2:
                # Show industries where this solution is used
                st.write("### Industry Applications")
                
                # Transform the single solution row to a more visual format
                solution_data = solution_row.melt(
                    id_vars=["AI Solution"], 
                    var_name="Industry",
                    value_name="Available"
                )
                solution_data = solution_data[solution_data["Industry"].isin(selected_industries)]
                
                # Create a horizontal bar chart
                solution_data["Value"] = solution_data["Available"].apply(lambda x: 1 if x == "✔" else 0)
                solution_data = solution_data.sort_values("Value", ascending=False)
                
                fig = go.Figure()
                
                # Add bars
                fig.add_trace(go.Bar(
                    y=solution_data["Industry"],
                    x=solution_data["Value"],
                    orientation='h',
                    marker=dict(
                        color=solution_data["Value"].map({1: '#22C55E', 0: '#CBD5E1'}),
                        line=dict(color='rgba(0,0,0,0)', width=1)
                    ),
                    hoverinfo='text',
                    hovertext=solution_data.apply(
                        lambda x: f"{x['Industry']}: {'Available' if x['Value'] == 1 else 'Not Available'}", 
                        axis=1
                    ),
                    textposition='auto',
                    text=solution_data["Available"]
                ))
                
                fig.update_layout(
                    title=f"{selected_solution} Industry Availability",
                    xaxis=dict(
                        showgrid=False,
                        showticklabels=False,
                        range=[0, 1]
                    ),
                    margin=dict(l=20, r=20, t=40, b=20),
                    height=400
                )
                fig = set_light_theme(fig)

                st.plotly_chart(fig, use_container_width=True)
                
                # Implementation examples or details
                st.markdown("#### Implementation Highlights")
                
                implementation_examples = {
                    "Chatbot": [
                        "Customer service automation reducing response time by 75%",
                        "Sales qualification increasing conversion rates by 15%",
                        "24/7 technical support coverage with 92% resolution rate"
                    ],
                    "IoT": [
                        "Predictive maintenance reducing downtime by 35%",
                        "Supply chain visibility improving delivery accuracy by 22%",
                        "Smart inventory management reducing holding costs by 18%"
                    ]
                }
                
                # if selected_solution in implementation_examples:
                #     for example in implementation_examples[selected_solution]:
                #         st.markdown(f"✅ {example}")
                # else:
                st.markdown("✅ Custom implementation available based on industry requirements")
                st.markdown("✅ Integration with existing systems and workflows")
                st.markdown("✅ Continuous improvement through machine learning")
            
        with tab3:
            # Industry focus
            st.markdown("### Industry AI Solution Profile")
            st.markdown("Analyze AI solution coverage by industry vertical")
            
            selected_industry = st.selectbox("Select Industry to Analyze", selected_industries)
            
            # Create industry profile
            industry_data = df[["AI Solution", selected_industry]]
            available_solutions = industry_data[industry_data[selected_industry] == "✔"]["AI Solution"].tolist()
            
            col1, col2 = st.columns([1, 1])
            
            with col1:
                st.markdown(f"### {selected_industry}")
                st.markdown(f"**Solutions available:** {len(available_solutions)}/{len(df)}")
                
                # Coverage percentage
                industry_coverage = len(available_solutions) / len(df) * 100
                st.progress(industry_coverage/100)
                st.caption(f"{industry_coverage:.1f}% solution coverage")
                
                # Show the list of available solutions for this industry
                st.markdown("#### Available AI Solutions")
                
                for solution in available_solutions:
                    st.markdown(f"✅ {solution}")
                    
            with col2:
                # Visualization for industry breakdown
                df_analysis = transform_data_for_analysis(df)
                industry_counts = df_analysis[selected_industry].sum()
                other_industries = [ind for ind in df_analysis.columns[1:] if ind != selected_industry]
                
                comparison_data = []
                for industry in other_industries:
                    count = df_analysis[industry].sum()
                    comparison_data.append({
                        "Industry": industry,
                        "Solution Count": count
                    })
                    
                comparison_df = pd.DataFrame(comparison_data)
                comparison_df = pd.concat([
                    pd.DataFrame([{"Industry": selected_industry, "Solution Count": industry_counts}]), 
                    comparison_df
                ])
                comparison_df = comparison_df.sort_values("Solution Count", ascending=False)
                
                fig = px.bar(
                    comparison_df,
                    x="Industry",
                    y="Solution Count",
                    color="Industry",
                    title="AI Solution Count by Industry",
                    color_discrete_sequence=px.colors.qualitative.Plotly
                )
                fig.update_layout(height=400, margin=dict(l=40, r=40, t=50, b=40))
                fig = set_light_theme(fig)
                st.plotly_chart(fig, use_container_width=True)
                
                # Add benchmark against industry average
                avg_solutions = df_analysis.iloc[:, 1:].sum().mean()
                # st.metric(
                #     label=f"{selected_industry} vs. Industry Average", 
                #     value=f"{industry_counts} Solutions",
                #     delta=f"{industry_counts - avg_solutions:.1f} vs. Avg"
                # )
        
        # Footer
        st.markdown("---")
        # footer_cols = st.columns([1, 1, 1])
        # with footer_cols[0]:
        #     st.markdown("**Contact:** ai-solutions@yourcompany.com")
        # with footer_cols[1]:
        #     st.markdown("**Documentation:** [View Solution Guide](https://example.com)")
        # with footer_cols[2]:
        #     st.markdown("**Last updated:** April 2, 2025")

if __name__ == "__main__":
    main()