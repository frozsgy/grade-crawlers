<h1>METU Grade Crawlers</h1>
<p>Suitable for downloading grades of all students taking any course from Mathmetics or Physics department, since they use their own system without any captcha validation.</p>
<h2>How to use</h2>
<p>The PHP script and the Python script basically do the same thing, so you can use whichever pleases you. The PHP one requires a mySQL database connection, however the Python one creates a csv file.</p>
<p>The first run basically iterates over the all possible student ID's to check if that student is taking that course. You need to update the cURL headers, the URL, and the regex to make the script work.</p>
<p>The second midterm file (mt2) uses the previously acquired user data from mt1 results, so the iteration takes way less than the first one.</p>
<p>Cheers!</p>
