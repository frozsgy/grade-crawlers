<h1>METU Grade Crawlers</h1>
<p>Suitable for downloading grades of all students taking any course from Mathematics or Physics department, since they use their own systems without any captcha validation.</p>
<h2>How to use</h2>
<p>The PHP script and the Python script basically do the same thing, so you can use whichever pleases you. The PHP one requires a mySQL database connection, however the Python one creates a csv file.</p>
<p>The first run basically iterates over the all possible student ID's to check if that student is taking that course. You need to update the cURL headers, the URL, and the regex to make the script work.</p>
<p>The second midterm file (mt2) uses the previously acquired user data from mt1 results, so the iteration takes way less than the first one.</p>
<h2>Finals Curve Generator</h2>
<p>I just added a new file named as <i>219_download_final.py</i>, which is basically an updated version of the MT2 file. It downloads everything as usual, then creates a CSV file with the related Excel formulas integrated. After that, all you need to do is to use the I<sup>th</sup> and J<sup>th</sup> columns to generate a graph, so you will be able to see the standart distribution of the grades. I believe it will work with the Turkish version of the MS Excel only, but it's quite easy to replace the formulas with the English ones, so you can make it work if you need to. </p>
<p>Cheers!</p>
