// memento pattern is used to store the state of an object
// so that it can be restored later on.
// It is one of the behavioral design patterns.
package memento;

public class Main {
    public static void main(String[] args) {
        Editor editor;
        editor = new Editor();
        var history = new History();

        editor.setContent("a");
        editor.setTitle("The return of the King!");
        history.push(editor.createState());

        editor.setContent("sohan");
        history.push(editor.createState());

        editor.setContent("c");
        editor.restore(history.pop());

        System.out.println(editor.getContent());
        System.out.println(editor.getTitle());
    }
}
