import React, { Component } from "react";
import { FaCocktail, FaHiking, FaShuttleVan, FaBeer,FaCoffee,FaSwimmer,FaWifi } from "react-icons/fa";
import Title from "./Title";
export default class Services extends Component {
  state = {
    services: [
      {
        icon: <FaCoffee />,
        title: "Free Breakfast",
        info:
          ""
      },
      {
        icon: <FaSwimmer />,
        title: "Swimming Pool",
        info:
          ""
      },
      {
        icon: <FaWifi />,
        title: "Free Wifi",
        info:
          ""
      },
      {
        icon: <FaBeer />,
        title: "Beverages",
        info:
          ""
      }
    ]
  };
  render() {
    return (
      <section className="services">
        <Title title="Hotel Elite Services" />
        <div className="services-center">
          {this.state.services.map(item => {
            return (
              <article key={`item-${item.title}`} className="service">
                <span>{item.icon}</span>
                <h6>{item.title}</h6>
                <p>{item.info}</p>
              </article>
            );
          })}
        </div>
      </section>
    );
  }
}
