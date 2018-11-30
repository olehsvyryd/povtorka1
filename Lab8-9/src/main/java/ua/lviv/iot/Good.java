package ua.lviv.iot;

import javax.persistence.*;

@Entity
public class Good {
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Id
    @Column(name = "id")
    private Integer id;

    @Column(name = "modelName")
    private String modelName;

    @Column(name = "sex")
    private Sex sex;

    @Column(name = "season")
    private Season season;

    @Column(name = "price")
    private double price;


    public Good() {
    }

    public Good(final String modelName, final Sex sex, final Season season, final double price) {
        this.modelName = modelName;
        this.sex = sex;
        this.season = season;
        this.price = price;
    }

    @SuppressWarnings("CheckStyle")
    @Override
    public String toString() {
        return " modelName='" + getModelName() + '\''
                + "sex='" + getSex() + '\''
                + "season='" + getSeason() + '\''
                + ", price=" + getPrice()
                + '\'';
    }

    public final String getModelName() {
        return modelName;
    }

    public final void setModelName(final String modelName) {
        this.modelName = modelName;
    }

    public final Sex getSex() {
        return sex;
    }

    public final void setSex(final Sex sex) {
        this.sex = sex;
    }

    public final Season getSeason() {
        return season;
    }

    public final void setSeason(final Season season) {
        this.season = season;
    }

    public final double getPrice() {
        return price;
    }

    public final void setPrice(final double price) {
        this.price = price;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }
}
