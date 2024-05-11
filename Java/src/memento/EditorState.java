package memento;

public class EditorState {
    // final means that the value of the variable cannot be changed
    private final String content;

    
    public EditorState(String content) {
        this.content = content;
    }

    public String getContent() {
        return content;
    }
}
