# rulefinder

Inspiration: looking at Baltimore city budget data from FY2021 in particular.  This budget table is structured with 99296 rows (each corresponding to a payment made to a vendor or contractor).  The columns are as follows:

['OBJECTID_1', 'OBJECTID', 'Date', 'Agency', 'Service',
       'Spending_Category', 'Spending_Description', 'Fund', 'Amount',
       'Vendor_Name', 'Date_Accuracy', 'name', 'GlobalID']

In other words we have interesting columns such as Agency, Service, Vendor Name, Spending Category, Fund, Amount, etc.

I initially poked at this code with numpy and pandas in a very exploratory way to get a feel for some of the data and structure, which raised more and more complicated questions about contents and structure.

First of all, many of these categories have some sort of "controlled vocabulary" which can become evident from examining the data.  For example, enumerating all the values that occur in the Fund column gives a list of funds from which city vendors/contractors are paid.  Spending Category/Spending Description gives an idea of how the city categorizes different payments.  And naturally being able to aggregate amounts by any of these categories is of interest in a budget such as this.  These are all pretty basic and obvious questions to ask when confronted with data like this, and they are particularly obvious given our external prior knowledge about the contents.

However, when poking around at this it also became obvious that there is some hidden structure that happens to apply to this database and others that is not immediately obvious.  For example, one might look at a particular vendor and notice that this vendor is always paid out of the same fund or paid by the same agency (which is trivially true if they only have one entry, of course).  Or it might be obvious that for a given fund only one agency is paying vendors/contractors from that fund.  This may be coincidental, but it may also point to some external reason for the data being structured in the way it is structured.

A broader question is this: for the data we have in this database, can we find a list of interesting potential "rules" that the data happen to conform to of the form:

When COLUMN A has value X then COLUMN B always has value Y.

It should be possible to find such statements.  As pointed out before, it is trivial to do so in the case where, say, a vendor has only one payment event that happened from one particular fund for one particular service.  It's a bit more interesting when you locate, for example, a vendor that services only the fire department and is always paid out of one particular equipment fund with hundreds of payments.

--------------------------------

This can be broadened beyond city budget of course, in which case some of the connections become very obvious and suggestive.  Suppose you have a database where some columns are portions of addresses (city state zip).  One "rule" that is likely to pop out of such a database is something like "IF THE CITY IS X THEN THE STATE IS ALWAYS Y", e.g. "If the city is Baltimore then the state is always Maryland".  You may get interesting rulebreakers or exceptions as well such as "If the city is KANSAS CITY then the state is always EITHER KANSAS OR MISSOURI".

--------------------------------
In any case, the initial data set is the city budget but the same logic can be used to discover potential rules about any structured data.

The goal is to find correlations and identify when they may be actually interesting.  The pandas package with dataframes (which conveniently associate names with columns etc) should make identifying and describing these particularly easy.
