export const styles: Record<string, React.CSSProperties> = {
    header: {
        position: "relative",
        backgroundColor: "#1E3A8A",
        color: "white",
        padding: "4rem 0",
        display: "flex",
        flexDirection: "column" as "column",
        alignItems: "center",
        justifyContent: "center",
        textAlign: "center",
    },
    logo: {
        width: "15rem",
        height: "auto",
    },
    content: {
        position: "relative",
        zIndex: 10,
        padding: "2rem",
        maxWidth: "1200px",
        margin: "0 auto",
    },
    title: {
        fontSize: "3rem",
        fontWeight: "bold",
        color: "#333",
        marginBottom: "1rem",
        textAlign: "center",
    },
    projectsBox: {
        display: "grid",
        gridTemplateColumns: "repeat(auto-fill, minmax(300px, 1fr))",
        gap: "2rem",
        padding: "1rem",
    },
    projectCard: {
        backgroundColor: "#E2E8F0",
        borderRadius: "8px",
        boxShadow: "0 4px 6px rgba(0, 0, 0, 0.1)",
        display: "flex",
        flexDirection: "column" as "column",
        justifyContent: "center",
        alignItems: "center",
        padding: "1rem",
        transition: "transform 0.3s ease, box-shadow 0.3s ease",
        cursor: "pointer",
        border: "none",
        outline: "none",
    },
    projectCardHover: {
        transform: "translateY(-10px)",
        boxShadow: "0 6px 12px rgba(0, 0, 0, 0.2)",
    },
    projectCardContent: {
        textAlign: "center" as "center",
    },
    projectName: {
        fontSize: "1.5rem",
        fontWeight: "600",
        marginBottom: "0.5rem",
    },
    projectDescription: {
        fontSize: "1rem",
        color: "#555",
    },
    createBox: {
        backgroundColor: "#E2E8F0",
        borderRadius: "8px",
        boxShadow: "0 4px 6px rgba(0, 0, 0, 0.1)",
        display: "flex",
        flexDirection: "column" as "column",
        justifyContent: "center",
        alignItems: "center",
        padding: "1rem",
        transition: "transform 0.3s ease, box-shadow 0.3s ease",
        cursor: "pointer",
        border: "none",
        outline: "none",
    },
    createBoxHover: {
        transform: "translateY(-10px)",
        boxShadow: "0 6px 12px rgba(0, 0, 0, 0.2)",
    },
    plusIcon: {
        fontSize: "3rem",
        fontWeight: "bold",
        color: "#1E3A8A",
    },
    form: {
        display: "flex",
        flexDirection: "column",
        gap: "1rem",
        maxWidth: "500px",
        margin: "0 auto",
        padding: "1rem",
        border: "1px solid #ddd",
        borderRadius: "8px",
        backgroundColor: "#f9f9f9",
    },
    input: {
        padding: "0.5rem",
        fontSize: "1rem",
        borderRadius: "4px",
        border: "1px solid #ccc",
    },
    button: {
        padding: "0.75rem 1.5rem",
        backgroundColor: "#1E3A8A",
        color: "white",
        border: "none",
        borderRadius: "4px",
        cursor: "pointer",
        fontSize: "1rem",
    },
};