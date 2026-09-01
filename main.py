import streamlit as st

st.set_page_config(page_title="لوحة تحكم الشركات الشاملة", layout="wide")

st.title("📊 لوحة التحكم المالية الشاملة للشركات بالمغرب")
st.write("أدخل البيانات المالية التفصيلية لشركتك لعرض المجموع الإجمالي والنسب الذكية بالدرهم المغربي:")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📥 مدخلات المبيعات والأرباح")
    company_name = st.text_input("اسم الشركة:", placeholder="مثال: شركة التميز للتجارة...")
    sales_q1 = st.number_input("مبيعات الربع الأول (DH):", min_value=0.0, value=10000.0)
    sales_q2 = st.number_input("مبيعات الربع الثاني (DH):", min_value=0.0, value=12000.0)
    sales_q3 = st.number_input("مبيعات الربع الثالث (DH):", min_value=0.0, value=15000.0)
    sales_q4 = st.number_input("مبيعات الربع الرابع (DH):", min_value=0.0, value=18000.0)

with col2:
    st.subheader("📤 مدخلات التكاليف والمصاريف")
    st.write("") 
    costs_q1 = st.number_input("مصاريف الربع الأول (DH):", min_value=0.0, value=4000.0)
    costs_q2 = st.number_input("مصاريف الربع الثاني (DH):", min_value=0.0, value=4500.0)
    costs_q3 = st.number_input("مصاريف الربع الثالث (DH):", min_value=0.0, value=5000.0)
    costs_q4 = st.number_input("مصاريف الربع الرابع (DH):", min_value=0.0, value=5500.0)

st.markdown("---")

if st.button("توليد التقرير المالي ومجموع الحسابات ⚙️"):
    if company_name:
        total_sales = sales_q1 + sales_q2 + sales_q3 + sales_q4
        total_costs = costs_q1 + costs_q2 + costs_q3 + costs_q4
        total_profit = total_sales - total_costs
        
        profit_margin = (total_profit / total_sales) * 100 if total_sales > 0 else 0
        
        st.success(f"🎉 تم حساب المجموع السنوي لشركة **{company_name}** بنجاح:")
        
        m1, m2, m3, m4 = st.columns(4)
        m1.metric(label="💰 مجموع المبيعات الكلي", value=f"{total_sales:,.2f} DH")
        m2.metric(label="📉 مجموع المصاريف الكلي", value=f"{total_costs:,.2f} DH")
        m3.metric(label="📈 صافي الأرباح الإجمالية", value=f"{total_profit:,.2f} DH")
        m4.metric(label="🎯 نسبة هامش الربح", value=f"{profit_margin:.1f} %")
        
        report_text = f"""--- تقرير المجموع المالي الشامل لشركة: {company_name} ---
مجموع المبيعات السنوية الكلي: {total_sales} درهم
مجموع المصاريف السنوية الكلي: {total_costs} درهم
صافي أرباح الشركة الإجمالية: {total_profit} درهم
نسبة هامش صافي الربح: {profit_margin:.1f}%
---------------------------------------
"""
        st.download_button(
            label="💾 تحميل تقرير المجموع الكلي للشركة",
            data=report_text,
            file_name=f"{company_name}_total_financial_report.txt",
            mime="text/plain"
        )
    else:
        st.warning("من فضلك أدخل اسم الشركة أولاً لتجهيز المجموع الحسابي.")
