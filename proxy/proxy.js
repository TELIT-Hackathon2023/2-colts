const express = require("express");
const axios = require("axios");

const app = express();
const port = 3001;

app.get("/api", async (req, res) => {
  try {
    const options = {
      method: "POST",
      url: "https://colts2.atlassian.net/rest/api/2/issue",
      params: { data: '"randomstring"' },
      headers: {
        "Content-Type": "application/json",
        Authorization:
          "Basic ZmlsaXBzaXBvQGdtYWlsLmNvbTpBVEFUVDN4RmZHRjBiRHBDSGJMODZVSjAzTXBONnBUNUdvNWs4bHZMT2FWczRvU2ZhdUpNdEdJSUl1VUNDSGRpNjZYQ29lVlVaU0NIWEdxUmhmLXhmOUJ6eVZWTWJxU3gyaU5EN0YyaDVER2dJRFVqdXpreURoblI1ZTNJbmlXREkxM3d5a2gtU1FaWXNSZE5MT0J2M1NGVzg2SVlra0xKcHZ0dnAtb3l1em1ndFFhUmY5SjFDOGM9Q0U0RjgzRUM=",
      },

      data: {
        fields: {
          project: { id: "10000" },
          issuetype: { id: "10001" },
          summary: `ml`,
          customfield_10032: { id: "10020", value: `low` },
          description: `please`,

          reporter: { id: "5e760f2a980acf0c2c352f08" },
          customfield_10021: [],
        },
        update: {},
        watchers: ["5e760f2a980acf0c2c352f08"],
      },
    };

    const response = await axios
      .request(options)
      .then(function (response) {
        console.log(response.data);
      })
      .catch(function (error) {
        console.error(error);
      });

    // Return the response from the external server to the frontend
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: "Internal Server Error" });
  }
});

app.listen(port, () => {
  console.log(`Proxy server is listening on port ${port}`);
});
