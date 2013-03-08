*** Problem Statement ***

Create a Django site that prototypes inventory control:

1. Allow user to see a list of available manufactures
2. Allow users to see inventory count on each manufactures
3. Allow users to place orders and inventory is automatically updated
4. Needs user authentication


*** Project Details ***

March 8, 2013:

1. Site is hosted on RedHat's OpenShift platform on the small free tier
https://django-ejpartners.rhcloud.com/inventory/manufactures/

2. DNS alias off my own domain with CNAME record:
https://esmee.pythonicneteng.com/inventory/manufactures/

3. Main code under ~/django/wsgi (OpenShift requirement)

4. Main site static file located under ~/django/wsgi (OpenShift requirement)

5. Main Django project under ~/django/wsgi/openshift

6. App under ~/django/wsgi/openshift/inventory

7. Manufactur main menu provides 2 functions, Search and Add Manufactures

8. Order tab requires authentication, use sales1/sales1.

9. Order pipeline is not completed, but prove of concept provided for the first two forms.

10. 'About Us' and 'Direction' are placeholders for now. 
