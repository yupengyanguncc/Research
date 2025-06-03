/**
 * This class demonstrates the difference between shallow and deep copying in Java.
 * It shows how object references work and why deep copying is important when you
 * want to create truly independent copies of objects.
 * 
 * The code includes examples of both shallow copying (where changes to the copy
 * affect the original) and deep copying (where the copy is completely independent).
 * 
 * @author Yupeng Yang
 * @version Jun 03, 2025
 */
public class Copy {
    public static class Address {
        String street;
        String city;
        
        public Address(String street, String city) {
            this.street = street;
            this.city = city;
        }
    }
    
    public static class Person {
        String name;
        Address address;
        
        public Person(String name, Address address) {
            this.name = name;
            this.address = address;
        }
    }

    public static void main(String[] args) {
        // Shallow copy example
        Person person1 = new Person("Yupeng", new Address("1234 Love Street", "Charlotte"));
        Person person2 = person1;  // Shallow copy

        // Modifying person2's address affects person1
        person2.address.city = "Harbin";
        System.out.println(person1.address.city);  // Prints "Harbin"

        System.out.println("--------------------------------");
        Person person3 = new Person("Yiru", new Address("4321 Love Street", "Auburn"));
        Person person4 = new Person(
            person3.name,
            new Address(person3.address.street, person3.address.city)
        );  // Deep copy

        // Modifying person4's address doesn't affect person3
        person4.address.city = "Harbin";
        System.out.println(person3.address.city);  // Still prints "Auburn"
    }
}
