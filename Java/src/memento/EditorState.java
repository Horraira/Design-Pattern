package memento;

public class EditorState {
    // final means that the value of the variable cannot be changed
    private final String content;
    private final String title;

    
    public EditorState(String content, String title) {
        this.content = content;
        this.title = title;
    }

    public String getContent() {
        return content;
    }

    public String getTitle() {
        return title;
    }
}
