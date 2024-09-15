# UUID

A **UUID** (Universally Unique Identifier) is a 128-bit identifier that is used to uniquely identify information in computer systems. It is designed to be unique across different systems and over time, minimizing the chances of duplication. UUIDs are commonly used in databases, distributed systems, and network protocols.

### Characteristics of a UUID:
1. **Uniqueness**: UUIDs are designed to be globally unique. The probability of generating two identical UUIDs is extremely low, making them suitable for use as unique identifiers in distributed systems.
2. **Format**: A UUID is typically represented as a 32-character hexadecimal string, separated by hyphens into five groups. The standard format is `8-4-4-4-12`, for a total of 36 characters (including hyphens). For example:
   ```
   123e4567-e89b-12d3-a456-426614174000
   ```
3. **Versions**: There are different versions of UUIDs, each with its method of generation:
   - **Version 1**: Based on the current timestamp and the MAC address of the computer.
   - **Version 2**: DCE Security version, which includes POSIX UIDs and GIDs.
   - **Version 3**: Name-based, using MD5 hashing.
   - **Version 4**: Randomly generated, which is the most commonly used.
   - **Version 5**: Name-based, using SHA-1 hashing.

### Common Uses of UUIDs:
- **Database Primary Keys**: UUIDs can be used as primary keys in databases to ensure uniqueness across distributed systems.
- **Unique Identifiers in URLs**: Used in URLs to uniquely identify resources without exposing sensitive information.
- **Session Tokens**: Used to uniquely identify user sessions in web applications.
- **File and Resource Identifiers**: Used to uniquely name files and other resources.

### Example in Python:
You can generate a UUID in Python using the `uuid` module:
```python
import uuid

# Generate a random UUID (version 4)
random_uuid = uuid.uuid4()
print(random_uuid)  # Output example: 3f2d1bc4-1df8-4de7-bfeb-8515dfb9e555
```

UUIDs are highly useful for ensuring the uniqueness of identifiers across different systems, 
especially in distributed environments where centralized coordination is not feasible.
