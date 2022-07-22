<h1> <span class="grey">&#60;</span> Notes <span class="grey">/></span> </h1>
<p>
    Created using: <span class="orange">HTML/CSS</span>, <span class="orange">Angular</span>,
        <span class="orange">TypeScript</span>, <span class="orange">Firebase</span>, <span class="orange">Python</span>,
        <span class="orange">Postgres SQL</span>
</p>

<p>
    I developed Rank<span class="grey">2</span>Earn in order to solve a specific business problem. During last year's crypto
    bull run, blockchain games - also known as 'play to earn' games - gained a lot of attention. As a result, sites like
    <a href="https://playtoearn.net/blockchaingames">playtoearn.net</a> got a lot of traffic from people trying to catch
    promising projects at an early stage. However, I couldn't find a way to check and compare community growth from all 
    these different projects - especially their discord server growth.
</p>
<p>
    That's the problem Rank<span class="grey">2</span>Earn solves. It keeps daily track of the projects' 
    Twitter and Discord. This way users can sort through and see which ones are growing fastest, have the biggest
    community or have staled their growth.
</p>

<h1> <span class="grey">></span> Project Structure</h1>

    ![r2e_project_structure](https://user-images.githubusercontent.com/100313927/180470306-4ffb1a64-8900-4ea6-af46-33694e7871fe.png)


<h1> <span class="grey">></span> Challenges</h1>
<p>
    Since this was my first project, even the basic things like setting up Angular and Firebase demanded time.
    Once done, the main challenges I faced was thinking of a way to organize the collected data.
</p>
<h2>Organizing data</h2>
    
    ![index_table](https://user-images.githubusercontent.com/100313927/180470390-34a49854-f860-492a-91d4-b2e1166d957a.png)

  
<p>
    To organize the collected data, I started by creating an 'index table', where each row has the necessary information 
    of a project plus an 'id' associated.
</p>
<p>
    These ids are used as reference to the name of the table that holds their data. For example, a project with an
    id of N will have its information found in tables 'table_N'(discord) and 'table_NF'(twitter).
    <br>
    <br>
</p>
    
    ![table_example](https://user-images.githubusercontent.com/100313927/180470501-7d8a1e6a-4731-47e7-85f2-79e4d7950664.png)

    
    <br>
    <br>
<h2>Data entry</h2>
<p>
    In order to feed the database new projects to keep track of, I first write the content that will go into the 'index table' to
    a 'add_file.xlsx'.
</p>
    
    ![add_file](https://user-images.githubusercontent.com/100313927/180470547-9122ab39-a3e6-4d5f-b310-fa9abf7cc5c7.png)

    
    <br>
    <br>
<p>
    Then, I run a python script to pop the repeated entries and add the ones that pass to the database. 
</p>
    <br>
    
    ![add_db](https://user-images.githubusercontent.com/100313927/180470597-8ee07cfb-90fa-418f-8fe5-b83b595d4cc8.png)

    

<h1> <span class="grey">></span> Endnotes</h1>
<p>
    There are lots of things I want to improve on in this project. The UI is looking very amateurish and the data is set statically.
    Moving forwards, I want to make it so the data updates dynamically, and the landing page to work as a 'discovery' tool.
</p>
<p>
    I think this was a very cool and challenging first project. Even though all the difficulties, I had a great time developing it.
    So much so that I decided to set my career path in this field - when I first started the project, I intended to simply make
    a business out of it, not a career move.
</p>
