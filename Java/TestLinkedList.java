import java.util.*;

public class TestLinkedList {

        public static void main(String[] args) {

                //LinkedList Instantiation
                LinkedList<Integer> list = new LinkedList<>();

                //appending to linkedlist
                list.add(10);
                list.add(20);
                list.add(30);

                System.out.println("First element :"+list.getFirst());

                for(Integer num : list){
                        System.out.println(num);
                }

	}
}
